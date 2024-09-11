import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db.database import Base

offset = datetime.timezone(datetime.timedelta(hours=4))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    password = Column(String)
    activeTeam = Column(String, nullable=True)
    online = Column(Boolean, default=False)
    active_team_id = Column('active_team_id', Integer(), ForeignKey('teams.id'), nullable=True)
    active_team = relationship("Team", back_populates="users")
    role_id = Column('role_id', Integer(), ForeignKey('roles.id'), nullable=False)
    role = relationship("Role", back_populates="users")
    history = relationship("FormHistory", back_populates="user")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    users = relationship("User", back_populates="role")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    color = Column(String)
    forms = relationship("Form", back_populates="team")
    users = relationship("User", back_populates="active_team")


class FormStatus(Base):
    __tablename__ = "forms_statuses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    color = Column(String, nullable=True)
    forms = relationship("Form", back_populates="status")


class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    dateBirth = Column(String, nullable=True)
    year = Column(String, nullable=True)
    passportWho = Column(String, nullable=True)
    passportDetail = Column(String, nullable=True)
    passportAddress = Column(String, nullable=True)
    passportAddressOld = Column(String, nullable=True)
    addressIndex = Column(String, nullable=True)
    placeBirth = Column(String, nullable=True)
    busPrice = Column(String, nullable=True)
    metroPrice = Column(String, nullable=True)
    job = Column(String, nullable=True)
    transferWho = Column(String, nullable=True)
    tenPayments = Column(String, nullable=True)
    salary = Column(String, nullable=True)
    ATMaddress = Column(String, nullable=True)
    bankGadgetPast = Column(String, nullable=True)
    bankDeposit = Column(String, nullable=True)
    education = Column(String, nullable=True)
    BankCardCity = Column(String, nullable=True)
    address = Column(String, nullable=True)
    addressPeople = Column(String, nullable=True)
    bankClientAt = Column(String, nullable=True)
    bankCredit = Column(String, nullable=True)
    bankPersonVisit = Column(String, nullable=True)
    bankGadget = Column(String, nullable=True)
    bankEmail = Column(String, nullable=True)
    code = Column(String, nullable=True)
    floorCount = Column(String, nullable=True)
    bankNumberNow = Column(String, nullable=True)
    bankNumberPast = Column(String, nullable=True)
    cardDetail = Column(String, nullable=True)
    additional = Column(String, nullable=True)
    images = Column(String, nullable=True)
    team_id = Column('team_id', Integer(), ForeignKey('teams.id'), nullable=True)
    team = relationship("Team", back_populates="forms")
    drop_manager_id = Column('drop_manager_id', Integer(), ForeignKey('drop_managers.id'), nullable=True)
    drop_manager = relationship("DropManager", back_populates="forms")
    status_id = Column('status_id', Integer(), ForeignKey(FormStatus.id), nullable=True)
    status = relationship("FormStatus", back_populates="forms")
    history = relationship("FormHistory", back_populates="form")


class FormHistory(Base):
    __tablename__ = "forms_history"

    id = Column(Integer, primary_key=True, index=True, nullable=True)
    form_id = Column('form_id', Integer(), ForeignKey(Form.id), nullable=True)
    user_id = Column('user_id', Integer(), ForeignKey(User.id), nullable=True)
    form = relationship("Form", back_populates="history")
    user = relationship("User", back_populates="history")
    date = Column(String, default=datetime.datetime.now(offset).strftime('%d.%m.%Y %H:%M'))


class DropManager(Base):
    __tablename__ = "drop_managers"

    id = Column(Integer, primary_key=True, index=True, nullable=True)
    name = Column(String, nullable=True)
    tg_id = Column(String, nullable=True)
    referral = Column(String, nullable=True)
    forms = relationship("Form", back_populates="drop_manager")


class TrainingFolder(Base):
    __tablename__ = "training_folder"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    link = Column(String, nullable=True)
    folder_id = Column('folder_id', Integer(), nullable=True)


class TrainingFile(Base):
    __tablename__ = "training_file"

    id = Column(Integer, primary_key=True, index=True)
    folder_id = Column('folder_id', Integer(), ForeignKey(TrainingFolder.id), nullable=True)
    name = Column(String, nullable=True)
    route = Column(String, nullable=True)


class ToDoCategory(Base):
    __tablename__ = "to_do_category"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)


class ToDoList(Base):
    __tablename__ = "to_do_list"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column('user_id', Integer(), ForeignKey(User.id), nullable=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    user_name = Column(String, nullable=True)
    category_id = Column('category_id', Integer(), ForeignKey(ToDoCategory.id), nullable=True)
    date = Column(String, default=datetime.datetime.now(offset).strftime('%d.%m.%Y %H:%M'))
    