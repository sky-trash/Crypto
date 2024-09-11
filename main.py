from typing import Annotated, Type, Optional, List

from fastapi import FastAPI, Depends, File, Form, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from config import config
from db import models, schemas
from db.database import SessionLocal
from db.models import Role
from service.auth import token, get_current_active_user, get_current_active_admin
from service.dropManager import create_drop_manager, get_drop_managers, get_drop_manager_by_referral, \
    delete_drop_manager, edit_drop_manager
from service.form import create_form, get_forms, get_form, delete_form, edit_form, add_images_to_form, \
    remove_images_from_form
from service.history import get_histories
from service.role import get_roles
from service.status import create_status, get_statuses, get_status, delete_status, edit_status
from service.team import create_team, get_teams, get_team, delete_team, edit_team
from service.user import create_user, get_users, edit_user, delete_user, edit_online_user
from service.trainingFolder import create_training_folder, get_training_folders, get_training_folders_id, get_training_folder, delete_training_folder, edit_training_folder
from service.trainingFile import create_training_file,  get_training_files, get_training_files_id, get_training_file, delete_training_file
from service.toDoCategory import create_to_do_category, get_to_do_categoryes, get_to_do_category, delete_to_do_category, edit_to_do_category
from service.toDoList import create_to_do_list, get_to_do_lists, get_to_do_list, delete_to_do_list, edit_to_do_list, get_to_do_lists_user



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


docs = '/api'

if config['APP_ENV'] == 'prod':
    docs = None

app = FastAPI(docs_url=docs, redoc_url=None)

app.mount("/static/images", StaticFiles(directory="static/images"), name="static")
app.mount("/static/files", StaticFiles(directory="static/files"), name="static")

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')  # Создание таблиц, базовых ролей и пользователей
async def startup_event():
    db = SessionLocal()
    all = db.query(models.User).filter(models.User.login == 'Все').first()
    admin = db.query(models.User).filter(models.User.login == 'admin').first()
    user = db.query(models.User).filter(models.User.login == 'user').first()
    roles = ['ROLE_ADMIN', 'ROLE_USER']
    statuses = ['В работе', 'Не в работе']
    to_do_category = ['На реализацию', 'В процессе', 'Выполнено']

    for role_title in roles:
        check_role = db.query(models.Role).filter(models.Role.title == role_title).first()
        if not check_role:
            role = models.Role(
                title=role_title
            )
            db.add(role)
            db.commit()
            db.refresh(role)

    for status_title in statuses:
        check_status = db.query(models.FormStatus).filter(models.FormStatus.title == status_title).first()
        if not check_status:
            status = models.FormStatus(
                title=status_title
            )
            db.add(status)
            db.commit()
            db.refresh(status)

    for category_title in to_do_category:
        check_category = db.query(models.ToDoCategory).filter(models.ToDoCategory.title == category_title).first()
        if not check_category:
            categ = models.ToDoCategory(
                title=category_title
            )
            db.add(categ)
            db.commit()
            db.refresh(categ)

    if not all:
        role_all = db.query(models.Role).filter(models.Role.title == 'ROLE_ADMIN').first()
        all = models.User(
            login='Все',
            password='$2a$10$niESc6fHnMIj24e1EBi0u.bh1earBcLqObQRuWITtSBkw4rQmSe4K',
            role_id=role_all.id
        )
        db.add(all)
        db.commit()
        db.refresh(all)
    if not admin:
        role_admin = db.query(models.Role).filter(models.Role.title == 'ROLE_ADMIN').first()
        admin = models.User(
            login='admin',
            password='$2a$10$niESc6fHnMIj24e1EBi0u.bh1earBcLqObQRuWITtSBkw4rQmSe4K',
            role_id=role_admin.id
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
    if not user:
        role_user = db.query(models.Role).filter(models.Role.title == 'ROLE_USER').first()
        user = models.User(
            login='user',
            password='$2a$10$niESc6fHnMIj24e1EBi0u.bh1earBcLqObQRuWITtSBkw4rQmSe4K',
            role_id=role_user.id
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    db.close()


@app.get("/", tags=["Root"], name='База')  # База
def read_root():
    return 'мальчик иди в жопу отсюда'


@app.post("/token", response_model=schemas.Token, tags=["Token"], name="Получить токен")  # Получить токен
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
):
    return await token(form_data, db)


# @app.post("/roles", response_model=schemas.Role, tags=["Role"], name="Создать новую роль")  # Создать новую роль
# async def create_role_handler(
#         current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
#         role: schemas.RoleCreate,
#         db: Session = Depends(get_db)
# ) -> schemas.Role:
#     return await create_role(role, db)


@app.get("/roles", response_model=list[schemas.Role], tags=["Role"], name="Получить все роли")  # Получить все роли
async def get_all_roles_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
) -> list[Type[Role]]:
    return await get_roles(db)


@app.post("/users", response_model=schemas.User, tags=["User"],
          name="Создать нового пользователя")  # Создать нового пользователя
async def create_user_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        user: schemas.UserCreate,
        db: Session = Depends(get_db)
):
    return await create_user(user, db)


@app.get("/users", response_model=list[schemas.User], tags=["User"],
         name="Получить всех пользователей")  # Получить всех пользователей
async def get_users_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await get_users(db)


@app.patch("/users/{user_id}", response_model=int, tags=["User"],
           name="Редактировать пользователя по идентификатору")
async def edit_team_handler(
        user_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        user: schemas.UserUpdate,
        db: Session = Depends(get_db)
):
    return await edit_user(db, user, user_id)


@app.patch("/users/{user_id}/online", response_model=int, tags=["User"],
           name="Редактировать пользователя по идентификатору")
async def edit_team_handler(
        user_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        user: schemas.UserUpdateOnline,
        db: Session = Depends(get_db)
):
    return await edit_online_user(db, user, user_id)


@app.get("/users/current", response_model=schemas.User, tags=["User"],
         name="Получить инфу о пользователе")  # Получить инфу о пользователе
async def get_user_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
):
    return current_user


@app.delete("/users/{user_id}", response_model=int, tags=["User"],
            name="Удалить пользователя по идентификатору")  # Удалить пользователя по идентификатору
async def delete_user_handler(
        user_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_user(db, user_id)


@app.post("/forms", response_model=schemas.Form, tags=["Form"], name="Создать новую анкету")  # Создать новую анкету
async def create_form_handler(
        images: List[Optional[Annotated[UploadFile, File()]]] = File(None),
        name: Optional[Annotated[str, Form()]] = Form(None),
        dateBirth: Optional[Annotated[str, Form()]] = Form(None),
        year: Optional[Annotated[str, Form()]] = Form(None),
        passportWho: Optional[Annotated[str, Form()]] = Form(None),
        passportDetail: Optional[Annotated[str, Form()]] = Form(None),
        passportAddress: Optional[Annotated[str, Form()]] = Form(None),
        passportAddressOld: Optional[Annotated[str, Form()]] = Form(None),
        addressIndex: Optional[Annotated[str, Form()]] = Form(None),
        placeBirth: Optional[Annotated[str, Form()]] = Form(None),
        busPrice: Optional[Annotated[str, Form()]] = Form(None),
        metroPrice: Optional[Annotated[str, Form()]] = Form(None),
        job: Optional[Annotated[str, Form()]] = Form(None),
        transferWho: Optional[Annotated[str, Form()]] = Form(None),
        tenPayments: Optional[Annotated[str, Form()]] = Form(None),
        salary: Optional[Annotated[str, Form()]] = Form(None),
        ATMaddress: Optional[Annotated[str, Form()]] = Form(None),
        bankGadgetPast: Optional[Annotated[str, Form()]] = Form(None),
        bankDeposit: Optional[Annotated[str, Form()]] = Form(None),
        education: Optional[Annotated[str, Form()]] = Form(None),
        BankCardCity: Optional[Annotated[str, Form()]] = Form(None),
        address: Optional[Annotated[str, Form()]] = Form(None),
        addressPeople: Optional[Annotated[str, Form()]] = Form(None),
        bankClientAt: Optional[Annotated[str, Form()]] = Form(None),
        bankCredit: Optional[Annotated[str, Form()]] = Form(None),
        bankPersonVisit: Optional[Annotated[str, Form()]] = Form(None),
        bankGadget: Optional[Annotated[str, Form()]] = Form(None),
        bankEmail: Optional[Annotated[str, Form()]] = Form(None),
        code: Optional[Annotated[str, Form()]] = Form(None),
        floorCount: Optional[Annotated[str, Form()]] = Form(None),
        bankNumberNow: Optional[Annotated[str, Form()]] = Form(None),
        bankNumberPast: Optional[Annotated[str, Form()]] = Form(None),
        cardDetail: Optional[Annotated[str, Form()]] = Form(None),
        additional: Optional[Annotated[str, Form()]] = Form(None),
        team_id: Optional[Annotated[str, Form()]] = Form(None),
        status_id: Optional[Annotated[str, Form()]] = Form(None),
        drop_manager_id: Optional[Annotated[str, Form()]] = Form(None),
        db: Session = Depends(get_db)
):
    return await create_form(name,
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
                             status_id, drop_manager_id, db, images)


@app.patch("/forms/add_images/{form_id}", response_model=int, tags=["Form"], name="Добавить фото к анкете")
async def create_form_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        form_id: int,
        images: List[Optional[Annotated[UploadFile, File()]]] = File(None),
        db: Session = Depends(get_db)
):
    return await add_images_to_form(db, form_id, images)


@app.patch("/forms/delete_images/{form_id}", response_model=int, tags=["Form"], name="удалить фото у анкеты")
async def create_form_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        form_id: int,
        images: schemas.FormImages,
        db: Session = Depends(get_db)
):
    return await remove_images_from_form(db, form_id, images)


@app.get("/forms", response_model=list[schemas.Form], tags=["Form"], name="Получить все анкеты")  # Получить все анкеты
async def get_forms_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),
        team_id: Optional[int] | None = None,
):
    return await get_forms(db, team_id)


@app.get("/forms/{form_id}", response_model=Optional[schemas.Form], tags=["Form"],
         name="Получить анкету по идентификатору")  # Получить анкету по идентификатору
async def get_forms_handler(
        form_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_form(db, form_id)


@app.delete("/forms/{form_id}", response_model=int, tags=["Form"],
            name="Удалить анкету по идентификатору")  # Удалить анкету по идентификатору
async def delete_form_handler(
        form_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_form(db, form_id)


@app.patch("/forms/{form_id}", response_model=int, tags=["Form"],
           name="Редактировать анкету по идентификатору")  # Редактировать анкету по идентификатору
async def edit_form_handler(
        form_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        form: schemas.FormUpdate,
        db: Session = Depends(get_db)
):
    return await edit_form(db, form, form_id, current_user.id)


@app.post("/teams", response_model=schemas.Team, tags=["Team"], name="Создать новую команду")  # Создать новую анкету
async def create_teams_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        team: schemas.TeamCreate,
        db: Session = Depends(get_db)
):
    return await create_team(team, db)


@app.get("/teams", response_model=list[schemas.Team], tags=["Team"], name="Получить все команды")  # Получить все анкеты
async def get_teams_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_teams(db)


@app.get("/teams/{team_id}", response_model=schemas.Team, tags=["Team"],
         name="Получить команду по идентификатору")  # Получить анкету по идентификатору
async def get_team_handler(
        team_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_team(db, team_id)


@app.delete("/teams/{team_id}", response_model=int, tags=["Team"],
            name="Удалить команду по идентификатору")  # Удалить анкету по идентификатору
async def delete_team_handler(
        team_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_team(db, team_id)


@app.patch("/teams/{team_id}", response_model=int, tags=["Team"],
           name="Редактировать команду по идентификатору")  # Редактировать анкету по идентификатору
async def edit_team_handler(
        team_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        team: schemas.TeamCreate,
        db: Session = Depends(get_db)
):
    return await edit_team(db, team, team_id)


@app.post("/statuses", response_model=schemas.FormStatus, tags=["Status"],
          name="Создать новый статус")  # Создать новую анкету
async def create_status_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        status: schemas.FormStatusCreate,
        db: Session = Depends(get_db)
):
    return await create_status(status, db)


@app.get("/statuses", response_model=list[schemas.FormStatus], tags=["Status"],
         name="Получить все статусы")  # Получить все анкеты
async def get_statuses_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_statuses(db)


@app.get("/statuses/{status_id}", response_model=schemas.FormStatus, tags=["Status"],
         name="Получить статус по идентификатору")  # Получить анкету по идентификатору
async def get_status_handler(
        status_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_status(db, status_id)


@app.delete("/statuses/{status_id}", response_model=int, tags=["Status"],
            name="Удалить статус по идентификатору")  # Удалить анкету по идентификатору
async def delete_status_handler(
        status_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_status(db, status_id)


@app.patch("/statuses/{status_id}", response_model=int, tags=["Status"],
           name="Редактировать статус по идентификатору")
async def edit_status_handler(
        status_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        status: schemas.FormStatusCreate,
        db: Session = Depends(get_db)
):
    return await edit_status(db, status, status_id)


@app.get("/histories/{form_id}", response_model=list[schemas.FormHistory], tags=["History"],
         name="Получить историю")
async def get_histories_handler(
        form_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_histories(db, form_id, current_user.id)


@app.post("/drop_managers", response_model=schemas.DropManager, tags=["DropManager"],
          name="Создать нового дроповода")
async def create_drop_manager_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        drop_manager: schemas.DropManagerCreate,
        db: Session = Depends(get_db)
):
    return await create_drop_manager(drop_manager, db)


@app.get("/drop_managers", response_model=list[schemas.DropManager], tags=["DropManager"],
         name="Получить всех дроповодов")
async def get_drop_managers_handler(
        db: Session = Depends(get_db)
):
    return await get_drop_managers(db)


@app.get("/drop_managers/{referral}", response_model=Optional[schemas.DropManager], tags=["DropManager"],
         name="Получить дропа по рефералке")
async def get_drop_manager_handler(
        referral: str,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_drop_manager_by_referral(db, referral)


@app.delete("/drop_managers/{drop_manager_id}", response_model=int, tags=["DropManager"],
            name="Удалить дроповода по идентификатору")
async def delete_drop_manager_handler(
        drop_manager_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_drop_manager(db, drop_manager_id)


@app.patch("/drop_managers/{drop_manager_id}", response_model=int, tags=["DropManager"],
           name="Редактировать дроповода по идентификатору")
async def edit_drop_manager_handler(
        drop_manager_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        drop_manager: schemas.DropManagerCreate,
        db: Session = Depends(get_db)
):
    return await edit_drop_manager(db, drop_manager, drop_manager_id)


@app.post("/training_folders", response_model=schemas.TrainingFolder, tags=["TrainingFolder"],
          name="Создание новой папки")
async def create_training_folder_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        training_folder: schemas.TrainingFolderCreate,
        db: Session = Depends(get_db)
):
    return await create_training_folder(db, training_folder)

@app.post("/training_folders/{training_folder_id}", response_model=schemas.TrainingFolder, tags=["TrainingFolder"],
          name="Создание новой папки")
async def create_training_folder_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        training_folder_id: int, 
        db: Session = Depends(get_db)
):
    return await create_training_folder(db, training_folder_id)


@app.get("/training_folders", response_model=List[schemas.TrainingFolder], tags=["TrainingFolder"],
         name="Получить все папки")
async def get_all_training_folders_handler(
        db: Session = Depends(get_db)
):
    return await get_training_folders(db)


@app.get("/training_folders/all/{id}", response_model=List[schemas.TrainingFolder], tags=["TrainingFolder"],
         name="Получить все папки по id")
async def get_all_training_folders_id_handler(
        id: int,
        db: Session = Depends(get_db)
):
    return await get_training_folders_id(db, id)    


@app.get("/training_folders/{training_folder_id}", response_model=Optional[schemas.TrainingFolder], tags=["TrainingFolder"],
         name="Получить папку по индификатору")
async def get_training_folder_handler(
        training_folder_id: int,
        current_user: schemas.User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return await get_training_folder(db, training_folder_id)


@app.delete("/training_folders/{training_folder_id}", response_model=int, tags=["TrainingFolder"],
            name="Удалить папку по идентификатору")
async def delete_training_folder_handler(
        training_folder_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_training_folder(db, training_folder_id)


@app.patch("/training_folders/{training_folder_id}", response_model=int, tags=["TrainingFolder"],
           name="Редактировать папку по идентификатору")
async def edit_training_folder_handler(
        training_folder_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        training_folder: schemas.TrainingFolderCreate,
        db: Session = Depends(get_db)
):
    return await edit_training_folder(db, training_folder, training_folder_id)



@app.post("/training_files", response_model=schemas.TrainingFile, tags=["TrainingFile"],
          name="Создать новый файл")
async def create_training_file_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        training_file: schemas.TrainingFileCreate,
        db: Session = Depends(get_db)
):
    return await create_training_file(db, training_file)

@app.post("/training_files/{training_folder_id}", response_model=schemas.TrainingFile, tags=["TrainingFile"],
          name="Создать новый файл внутри папки")
async def create_training_file_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        training_file: schemas.TrainingFileCreate,
        training_folder_id: int,
        db: Session = Depends(get_db)
):
    return await create_training_file(db, training_file, training_folder_id)


@app.get("/training_files", response_model=List[schemas.TrainingFile], tags=["TrainingFile"],
         name="Получить все файлы")
async def get_all_training_files_handler(
        db: Session = Depends(get_db)
):
    return await get_training_files(db)


@app.get("/training_files/{training_file_id}", response_model=Optional[schemas.TrainingFile], tags=["TrainingFile"],
         name="Получить файл по индификатору")
async def get_all_training_files_handler(
        training_file_id: int,
        current_user: schemas.User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return await get_training_file(db, training_file_id)

@app.get("/training_files/all/{id}", response_model=List[schemas.TrainingFile], tags=["TrainingFile"],
         name="Получить все файлы по id")
async def get_all_training_files_id_handler(
        id: int,
        db: Session = Depends(get_db)
):
    return await get_training_files_id(db, id)


@app.delete("/training_files/{training_file_id}", response_model=int, tags=["TrainingFile"],
            name="Удалить файл по идентификатору")
async def delete_training_file_handler(
        training_file_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_training_file(db, training_file_id)


@app.post("/to_do_category", response_model=schemas.ToDoCategory, tags=["ToDoCategory"],
          name="Создать новую категорию")
async def create_to_do_category_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        to_do_category: schemas.ToDoListCreate,
        db: Session = Depends(get_db)
):
    return await create_to_do_category(to_do_category, db)


@app.get("/to_do_category", response_model=List[schemas.ToDoCategory], tags=["ToDoCategory"],
         name="Получить все категории")
async def get_all_to_do_category_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_to_do_categoryes(db)


@app.get("/to_do_category/{to_do_category_id}", response_model=schemas.ToDoCategory, tags=["ToDoCategory"],
         name="Получить категорию по идентификатору") 
async def get_to_do_category_handler(
        to_do_category_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db)
):
    return await get_to_do_category(db, to_do_category_id)


@app.delete("/to_do_category/{to_do_category_id}", response_model=int, tags=["ToDoCategory"],
            name="Удалить категорию по идентификатору")
async def delete_to_do_category_handler(
        to_do_category_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_to_do_category(db, to_do_category_id)


@app.patch("/to_do_category/{to_do_category_id}", response_model=int, tags=["ToDoCategory"],
           name="Редактировать категорию по идентификатору")
async def edit_to_do_category_handler(
        to_do_category_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        to_do_category: schemas.FormStatusCreate,
        db: Session = Depends(get_db)
):
    return await edit_to_do_category(db, to_do_category, to_do_category_id)


@app.post("/to_do_list", response_model=schemas.ToDoList, tags=["ToDoList"],
          name="Создание новой задачи")
async def create_to_do_list_handler(
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        to_do_list: schemas.ToDoListCreate,
        db: Session = Depends(get_db)
):
    return await create_to_do_list(to_do_list, db)


@app.get("/to_do_list", response_model=List[schemas.ToDoList], tags=["ToDoList"],
         name="Получить все задачи")
async def get_to_do_lists_handler(
        db: Session = Depends(get_db)
):
    return await get_to_do_lists(db)
    

@app.get("/to_do_list/{to_do_list_id}", response_model=Optional[schemas.ToDoList], tags=["ToDoList"],
         name="Получить задачи по индификатору")
async def get_to_do_list_handler(
        to_do_list_id: int,
        current_user: schemas.User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return await get_to_do_list(db, to_do_list_id)

@app.get("/to_do_list/users/{to_do_list_user_id}", response_model=List[schemas.ToDoList], tags=["ToDoList"],
         name="Получить задачи по пользователю")
async def get_to_do_list_user_handler(
        to_do_list_user_id: int,
        current_user: schemas.User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return await get_to_do_lists_user(db, to_do_list_user_id)

@app.delete("/to_do_list/{to_do_list_id}", response_model=int, tags=["ToDoList"],
            name="Удалить задачу по идентификатору")
async def delete_to_do_list_handler(
        to_do_list_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        db: Session = Depends(get_db)
):
    return await delete_to_do_list(db, to_do_list_id)


@app.patch("/to_do_list/{to_do_list_id}", response_model=int, tags=["ToDoList"],
           name="Редактировать задачу по идентификатору")
async def edit_to_do_list_handler(
        to_do_list_id: int,
        current_user: Annotated[schemas.User, Depends(get_current_active_admin)],
        to_do_list: schemas.ToDoListCreate,
        db: Session = Depends(get_db)
):
    return await edit_to_do_list(db, to_do_list, to_do_list_id)
