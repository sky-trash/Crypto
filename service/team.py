import json
from typing import Type
from sqlalchemy.orm import Session
from db import schemas, models


async def create_team(team: schemas.TeamCreate, db: Session) -> schemas.Team:
    db_team = models.Team(
        title=team.title,
        color=team.color,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


async def get_teams(db: Session) -> list[Type[schemas.Team]]:
    return db.query(models.Team).all()


async def get_team(db: Session, team_id: int) -> Type[schemas.Team] | None:
    return db.query(models.Team).filter(models.Team.id == team_id).first()


async def delete_team(db: Session, team_id: int) -> int:
    delete_team_db = db.query(models.Team).filter(models.Team.id == team_id).delete()
    db.commit()
    return delete_team_db


async def edit_team(db: Session, team: schemas.TeamCreate, team_id: int) -> int:
    update_data = team.model_dump(exclude_unset=True)
    updated_team = db.query(models.Team).filter(models.Team.id == team_id).update(update_data)
    db.commit()
    return updated_team
