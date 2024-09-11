import uuid
from typing import Type

from sqlalchemy.orm import Session

from db import schemas, models


async def create_drop_manager(drop_manager: schemas.DropManagerCreate, db: Session) -> schemas.DropManagerCreate:
    uuid_data = uuid.uuid4().hex
    db_drop_manager = models.DropManager(
        name=drop_manager.name,
        tg_id=drop_manager.tg_id,
        referral=uuid_data
    )
    db.add(db_drop_manager)
    db.commit()
    db.refresh(db_drop_manager)
    return db_drop_manager


async def get_drop_managers(db: Session) -> list[Type[schemas.Drop]]:
    return db.query(models.DropManager).all()


async def get_drop_manager_by_referral(db: Session, referral: str) -> Type[schemas.DropManager] | None:
    return db.query(models.DropManager).filter(models.DropManager.referral == referral).first()


async def delete_drop_manager(db: Session, drop_manager_id: int) -> int:
    delete_drop_manager_db = db.query(models.DropManager).filter(models.DropManager.id == drop_manager_id).delete()
    db.commit()
    return delete_drop_manager_db


async def edit_drop_manager(db: Session, drop_manager: schemas.DropManagerCreate, drop_manager_id: int) -> int:
    update_data = drop_manager.model_dump(exclude_unset=True)
    updated_drop_manager = db.query(models.DropManager).filter(models.DropManager.id == drop_manager_id).update(update_data)
    db.commit()
    return updated_drop_manager
