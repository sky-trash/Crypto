import json
from typing import Type, List, Optional
from sqlalchemy.orm import Session
from db import schemas, models


async def create_training_file(db: Session, training_file: schemas.TrainingFileCreate, folder_id: int | None = None) -> schemas.TrainingFile:
    db_training_file = models.TrainingFile(
        name=training_file.name,
        folder_id=folder_id,
        route=training_file.route,
    )
    db.add(db_training_file)
    db.commit()
    db.refresh(db_training_file)
    return db_training_file


async def get_training_files(db: Session) -> List[schemas.TrainingFile]:
    return db.query(models.TrainingFile).where(models.TrainingFile.folder_id.is_(None)).all()


async def get_training_files_id(db: Session, id: int) -> List[schemas.TrainingFile]:
    return db.query(models.TrainingFile).filter(models.TrainingFile.folder_id == id).all()
    

async def get_training_file(db: Session, training_file_id: int) -> Optional[schemas.TrainingFile]:
    return db.query(models.TrainingFile).filter(models.TrainingFile.id == training_file_id).first()


async def delete_training_file(db: Session, training_file_id: int) -> int:
    delete_training_file_db = db.query(models.TrainingFile).filter(models.TrainingFile.id == training_file_id).delete()
    db.commit()
    return delete_training_file_db
