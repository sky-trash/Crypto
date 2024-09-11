from typing import List, Type

from sqlalchemy.orm import Session
from db import models, schemas
from db.models import Role


async def create_role(role: schemas.RoleCreate, db: Session) -> schemas.Role:
    db_role = models.Role(
        title=role["title"],
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


async def get_roles(db: Session) -> list[Type[Role]]:
    return db.query(models.Role).all()
