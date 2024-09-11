import json
from typing import Type, List, Optional
from sqlalchemy.orm import Session
from db import schemas, models


async def create_training_folder(db: Session, training_folder: schemas.TrainingFolderCreate) -> schemas.TrainingFolder:
    db_trining_folder = models.TrainingFolder(
        name=training_folder.name,
        link=training_folder.link,
    )
    db.add(db_trining_folder)
    db.commit()
    db.refresh(db_trining_folder)
    return db_trining_folder


async def get_training_folders(db: Session) -> List[schemas.TrainingFolder]:
    return db.query(models.TrainingFolder).all()


async def get_training_folders_id(db: Session, id: int) -> List[schemas.TrainingFolder]:
    return db.query(models.TrainingFolder).filter(models.TrainingFolder.folder_id == id).all()


async def get_training_folder(db: Session, training_folder_id: int) -> Optional[schemas.TrainingFolder]:
    return db.query(models.TrainingFolder).filter(models.TrainingFolder.id == training_folder_id).first()


async def delete_training_folder(db: Session, training_folder_id: int) -> int:
    delete_training_folder_db = db.query(models.TrainingFolder).filter(models.TrainingFolder.id == training_folder_id).delete()
    db.commit()
    return delete_training_folder_db


async def edit_training_folder(db: Session, training_folder: schemas.TrainingFolderCreate, training_folder_id: int) -> int:
    update_data = training_folder.model_dump(exclude_unset=True)
    updated_training_folder = db.query(models.TrainingFolder).filter(models.TrainingFolder.id == training_folder_id).update(update_data)
    db.commit()
    return updated_training_folder