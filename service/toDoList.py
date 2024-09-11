import json
from typing import Type, List, Optional
from sqlalchemy.orm import Session
from db import schemas, models


async def create_to_do_list(to_do_list: schemas.ToDoListCreate, db: Session) -> schemas.ToDoList:
    db_to_do_list = models.ToDoList(
    user_id=to_do_list.user_id,
    title=to_do_list.title,
    description=to_do_list.description,
    user_name=to_do_list.user_name,
    category_id=to_do_list.category_id,
    )
    db.add(db_to_do_list)
    db.commit()
    db.refresh(db_to_do_list)
    return db_to_do_list



async def get_to_do_lists(db: Session) -> List[schemas.ToDoList]:
    return db.query(models.ToDoList).all()


async def get_to_do_list(db: Session, to_do_list_id: int) -> Optional[schemas.ToDoList]:
    return db.query(models.ToDoList).filter(models.ToDoList.id == to_do_list_id).first()


async def get_to_do_lists_user(db: Session, to_do_list_user_id: int) -> List[schemas.ToDoList]:
    return db.query(models.ToDoList).filter(models.ToDoList.user_id == to_do_list_user_id).all()


async def delete_to_do_list(db: Session, to_do_list_id: int) -> int:
    delete_to_do_list_db = db.query(models.ToDoList).filter(models.ToDoList.id == to_do_list_id).delete()
    db.commit()
    return delete_to_do_list_db


async def edit_to_do_list(db: Session, to_do_list: schemas.ToDoListCreate, to_do_list_id: int) -> int:
    update_data = to_do_list.model_dump(exclude_unset=True)
    updated_to_do_list = db.query(models.ToDoList).filter(models.ToDoList.id == to_do_list_id).update(update_data)
    db.commit()
    return updated_to_do_list