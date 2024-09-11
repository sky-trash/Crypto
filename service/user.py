from typing import Type

import bcrypt
from sqlalchemy.orm import Session

from db import models, schemas
from db.models import User


async def create_user(user: schemas.UserCreate, db: Session) -> schemas.User:
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(user.password.encode(), salt).decode('utf-8')
    db_account = models.User(
        login=user.login,
        password=hashed_password,
        role_id=user.role_id,
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


async def get_users(db: Session) -> list[Type[User]]:
    return db.query(models.User).all()


async def get_user(db: Session, user_id: int) -> Type[schemas.User] | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


async def delete_user(db: Session, user_id: int) -> int:
    delete_user_db = db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return delete_user_db


async def edit_user(db: Session, user: schemas.UserUpdate, user_id: int) -> int:
    salt = bcrypt.gensalt(10)
    update_data = user.model_dump(exclude_unset=True)
    if update_data.get('password'):
        update_data['password'] = bcrypt.hashpw(update_data['password'].encode(), salt).decode('utf-8')
    updated_user = db.query(models.User).filter(models.User.id == user_id).update(update_data)
    db.commit()
    return updated_user


async def edit_online_user(db: Session, user: schemas.UserUpdateOnline, user_id: int) -> int:
    update_data = user.model_dump(exclude_unset=True)
    updated_user = db.query(models.User).filter(models.User.id == user_id).update(update_data)
    db.commit()
    return updated_user
