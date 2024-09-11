import json
from typing import Type, List, Optional
from sqlalchemy.orm import Session
from db import schemas, models


async def create_to_do_category(to_do_category: schemas.ToDoCategoryCreate, db: Session) -> schemas.ToDoCategory:
    db_to_do_category = models.ToDoCategory(
        title=to_do_category.title,
    )
    db.add(db_to_do_category)
    db.commit()
    db.refresh(db_to_do_category)
    return db_to_do_category


async def get_to_do_categoryes(db: Session) -> List[Type[schemas.ToDoCategory]]:
    return db.query(models.ToDoCategory).all()


async def get_to_do_category(db: Session, to_do_category_id: int) -> Optional[schemas.ToDoCategory]:
    return db.query(models.ToDoCategory).filter(models.ToDoCategory.id == to_do_category_id).first()


async def delete_to_do_category(db: Session, to_do_category_id: int) -> int:
    delete_to_do_category_db = db.query(models.ToDoCategory).filter(models.ToDoCategory.id == to_do_category_id).delete()
    db.commit()
    return delete_to_do_category_db


async def edit_to_do_category(db: Session, to_do_category: schemas.ToDoCategoryCreate, to_do_category_id: int) -> int:
    update_data = to_do_category.model_dump(exclude_unset=True)
    updated_to_do_category = db.query(models.ToDoCategory).filter(models.ToDoCategory.id == to_do_category_id).update(update_data)
    db.commit()
    return updated_to_do_category
