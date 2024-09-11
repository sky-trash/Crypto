from typing import Type

from sqlalchemy.orm import Session

from db import schemas, models


async def create_status(status: schemas.FormStatusCreate, db: Session) -> schemas.FormStatus:
    db_status = models.FormStatus(
        title=status.title,
        color=status.color
    )
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


async def get_statuses(db: Session) -> list[Type[schemas.FormStatus]]:
    return db.query(models.FormStatus).all()


async def get_status(db: Session, status_id: int) -> Type[schemas.FormStatus] | None:
    return db.query(models.FormStatus).filter(models.FormStatus.id == status_id).first()


async def delete_status(db: Session, status_id: int) -> int:
    delete_status_db = db.query(models.FormStatus).filter(models.FormStatus.id == status_id).delete()
    db.commit()
    return delete_status_db


async def edit_status(db: Session, status: schemas.FormStatusCreate, status_id: int) -> int:
    update_data = status.model_dump(exclude_unset=True)
    updated_status = db.query(models.FormStatus).filter(models.FormStatus.id == status_id).update(update_data)
    db.commit()
    return updated_status
