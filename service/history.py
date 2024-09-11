from typing import Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from db import schemas, models


async def create_history(history: schemas.FormHistoryCreate, db: Session) -> schemas.FormHistory:
    db_history = models.FormHistory(
        user_id=history.user_id,
        form_id=history.form_id,
    )
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history


async def get_histories(db: Session, form_id: int, user_id: int) -> list[Type[schemas.FormHistory]]:
    if not form_id or not user_id:
        raise HTTPException(status_code=400, detail=f"form_id and user_id required")
    return db.query(models.FormHistory).filter(models.FormHistory.form_id == form_id, models.FormHistory.user_id == user_id).all()


async def delete_history(db: Session, history_id: int) -> int:
    delete_history_db = db.query(models.FormHistory).filter(models.FormHistory.id == history_id).delete()
    db.commit()
    return delete_history_db
