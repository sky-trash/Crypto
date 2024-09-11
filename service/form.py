import os
import uuid
from typing import Type, Optional, List

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from db import schemas, models


async def create_form(name,
                      dateBirth,
                      year,
                      passportWho,
                      passportDetail,
                      passportAddress,
                      passportAddressOld,
                      addressIndex,
                      placeBirth,
                      busPrice,
                      metroPrice,
                      job,
                      transferWho,
                      tenPayments,
                      salary,
                      ATMaddress,
                      bankGadgetPast,
                      bankDeposit,
                      education,
                      BankCardCity,
                      address,
                      addressPeople,
                      bankClientAt,
                      bankCredit,
                      bankPersonVisit,
                      bankGadget,
                      bankEmail,
                      code,
                      floorCount,
                      bankNumberNow,
                      bankNumberPast,
                      cardDetail,
                      additional,
                      team_id,
                      status_id, drop_manager_id, db: Session, images: List[UploadFile] | None = None) -> schemas.Form:
    images_names = []
    if not images:
        images = []
    for image in images:
        image_name = f"static/images/{uuid.uuid4().hex}.{image.filename.split('.')[-1]}"
        with open(image_name, 'wb') as f:
            f.write(await image.read())
        images_names.append(image_name)
    if team_id or team_id == 0:
        check_team = db.query(models.Team).filter(models.Team.id == team_id).first()
        if not check_team:
            raise HTTPException(status_code=400, detail=f"team with id {team_id} not found")
    if not len(images):
        images_names = None
    else:
        images_names = ','.join(images_names)
    db_form = models.Form(
        name=name,
        dateBirth=dateBirth,
        year=year,
        passportWho=passportWho,
        passportDetail=passportDetail,
        passportAddress=passportAddress,
        passportAddressOld=passportAddressOld,
        addressIndex=addressIndex,
        placeBirth=placeBirth,
        busPrice=busPrice,
        metroPrice=metroPrice,
        job=job,
        transferWho=transferWho,
        tenPayments=tenPayments,
        salary=salary,
        ATMaddress=ATMaddress,
        bankGadgetPast=bankGadgetPast,
        bankDeposit=bankDeposit,
        education=education,
        BankCardCity=BankCardCity,
        address=address,
        addressPeople=addressPeople,
        bankClientAt=bankClientAt,
        bankCredit=bankCredit,
        bankPersonVisit=bankPersonVisit,
        bankGadget=bankGadget,
        bankEmail=bankEmail,
        code=code,
        floorCount=floorCount,
        bankNumberNow=bankNumberNow,
        bankNumberPast=bankNumberPast,
        cardDetail=cardDetail,
        additional=additional,
        team_id=team_id,
        status_id=status_id,
        images=images_names,
        drop_manager_id=drop_manager_id,
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    if len(images):
        db_form.images = db_form.images.split(',')
    return db_form


async def add_images_to_form(db: Session, form_id: int, images: list[UploadFile]):
    form = db.query(models.Form).filter(models.Form.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    if not form.images:
        images_names = []
    else:
        images_names = form.images.split(',')
    for image in images:
        image_name = f"static/images/{uuid.uuid4().hex}.{image.filename.split('.')[-1]}"
        with open(image_name, 'wb') as f:
            f.write(await image.read())
        images_names.append(image_name)
    images_names = ','.join(images_names)
    data = {
        'images': images_names
    }
    updated_form = db.query(models.Form).filter(models.Form.id == form_id).update(data)
    db.commit()
    return updated_form


async def remove_images_from_form(db: Session, form_id: int, images: schemas.FormImages):
    form = db.query(models.Form).filter(models.Form.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    images_names = form.images.split(',')
    res = []
    for i in images_names:
        if i in images.images:
            os.unlink(i)
        else:
            res.append(i)
    if not res:
        res = None
    else:
        res = ','.join(res)
    data = {
        'images': res
    }
    updated_form = db.query(models.Form).filter(models.Form.id == form_id).update(data)
    db.commit()
    return updated_form


async def get_forms(db: Session, team_id: Optional[int] | None = False) -> list[Type[schemas.Form]]:
    forms = db.query(models.Form).filter(models.Form.team_id == team_id).all()
    if not team_id:
        forms = db.query(models.Form).all()
    for form in forms:
        if form.images:
            form.images = form.images.split(',')
        print(form.images)
    return forms


async def get_form(db: Session, form_id: int) -> Type[schemas.Form] | None:
    form = db.query(models.Form).filter(models.Form.id == form_id).first()
    if not form:
        return None
    if form.images:
        form.images = form.images.split(',')
    return form


async def delete_form(db: Session, form_id: int) -> int:
    delete_form_db = db.query(models.Form).filter(models.Form.id == form_id).first()
    db.delete(delete_form_db)
    db.commit()
    return 1


async def edit_form(db: Session, form: schemas.FormUpdate, form_id: int, user_id: int) -> int:
    update_data = form.model_dump(exclude_unset=True)
    updated_form = db.query(models.Form).filter(models.Form.id == form_id).update(update_data)
    db.commit()
    if updated_form:
        db_form_history = models.FormHistory(
            form_id=form_id,
            user_id=user_id
        )
        db.add(db_form_history)
        db.commit()
        db.refresh(db_form_history)
    return updated_form
