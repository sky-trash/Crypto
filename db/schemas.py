from pydantic import BaseModel


class RoleCreate(BaseModel):
    title: str


class Role(BaseModel):
    id: int
    title: str


class FormStatus(BaseModel):
    id: int
    title: str
    color: str | None = None


class FormStatusCreate(BaseModel):
    title: str
    color: str | None = None


class TeamCreate(BaseModel):
    title: str
    color: str


class Team(BaseModel):
    id: int
    title: str
    color: str


class FormTeam(BaseModel):
    id: int
    title: str
    color: str


class DropCreate(BaseModel):
    name: str | None = None
    color: str | None = None


class Drop(BaseModel):
    id: int
    name: str | None = None
    uuid: str | None = None
    color: str | None = None


class DropManagerCreate(BaseModel):
    name: str | None = None
    tg_id: str | None = None


class DropManager(BaseModel):
    id: int
    name: str | None = None
    tg_id: str | None = None
    referral: str | None = None


class FormCreate(BaseModel):
    name: str | None = None
    dateBirth: str | None = None
    year: str | None = None
    passportWho: str | None = None
    passportDetail: str | None = None
    passportAddress: str | None = None
    passportAddressOld: str | None = None
    addressIndex: str | None = None
    placeBirth: str | None = None
    busPrice: str | None = None
    metroPrice: str | None = None
    job: str | None = None
    transferWho: str | None = None
    tenPayments: str | None = None
    salary: str | None = None
    ATMaddress: str | None = None
    bankGadgetPast: str | None = None
    bankDeposit: str | None = None
    education: str | None = None
    BankCardCity: str | None = None
    address: str | None = None
    addressPeople: str | None = None
    bankClientAt: str | None = None
    bankCredit: str | None = None
    bankPersonVisit: str | None = None
    bankGadget: str | None = None
    bankEmail: str | None = None
    code: str | None = None
    floorCount: str | None = None
    bankNumberNow: str | None = None
    bankNumberPast: str | None = None
    cardDetail: str | None = None
    additional: str | None = None
    images: list[str] | None = None
    team_id: int | None = None
    status_id: int | None = None
    drop_manager_id: int | None = None


class FormUpdate(BaseModel):
    name: str | None = None
    dateBirth: str | None = None
    year: str | None = None
    passportWho: str | None = None
    passportDetail: str | None = None
    passportAddress: str | None = None
    passportAddressOld: str | None = None
    addressIndex: str | None = None
    placeBirth: str | None = None
    busPrice: str | None = None
    metroPrice: str | None = None
    job: str | None = None
    transferWho: str | None = None
    tenPayments: str | None = None
    salary: str | None = None
    ATMaddress: str | None = None
    bankGadgetPast: str | None = None
    bankDeposit: str | None = None
    education: str | None = None
    BankCardCity: str | None = None
    address: str | None = None
    addressPeople: str | None = None
    bankClientAt: str | None = None
    bankCredit: str | None = None
    bankPersonVisit: str | None = None
    bankGadget: str | None = None
    bankEmail: str | None = None
    code: str | None = None
    floorCount: str | None = None
    bankNumberNow: str | None = None
    bankNumberPast: str | None = None
    cardDetail: str | None = None
    additional: str | None = None
    team_id: int | None = None
    status_id: int | None = None
    drop_manager_id: int | None = None


class Form(BaseModel):
    id: int
    name: str | None = None
    dateBirth: str | None = None
    year: str | None = None
    passportWho: str | None = None
    passportDetail: str | None = None
    passportAddress: str | None = None
    passportAddressOld: str | None = None
    addressIndex: str | None = None
    placeBirth: str | None = None
    busPrice: str | None = None
    metroPrice: str | None = None
    job: str | None = None
    transferWho: str | None = None
    tenPayments: str | None = None
    salary: str | None = None
    ATMaddress: str | None = None
    bankGadgetPast: str | None = None
    bankDeposit: str | None = None
    education: str | None = None
    BankCardCity: str | None = None
    address: str | None = None
    addressPeople: str | None = None
    bankClientAt: str | None = None
    bankCredit: str | None = None
    bankPersonVisit: str | None = None
    bankGadget: str | None = None
    bankEmail: str | None = None
    code: str | None = None
    floorCount: str | None = None
    bankNumberNow: str | None = None
    bankNumberPast: str | None = None
    cardDetail: str | None = None
    additional: str | None = None
    images: list[str] | None = None
    team: FormTeam | None = None
    drop_manager: DropManager | None = None
    status: FormStatus | None = None


class UserCreate(BaseModel):
    login: str
    password: str
    role_id: int


class FormImages(BaseModel):
    images: list[str]


class UserUpdate(BaseModel):
    login: str | None = None
    password: str | None = None
    role_id: int | None = None
    active_team_id: str | int | None = None


class UserUpdateOnline(BaseModel):
    online: bool | None = None


class User(BaseModel):
    id: int
    login: str
    password: str
    online: bool | None = None
    active_team: Team | None = None
    role: Role


class FormHistory(BaseModel):
    id: int
    user: User
    date: str


class FormHistoryCreate(BaseModel):
    form_id: int
    user_id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: str | None = None
    role: Role | None = None


class TrainingFolder(BaseModel):
    id: int
    name: str 
    link: str | None = None
    folder_id: int | None = None


class TrainingFolderCreate(BaseModel):
    name: str 
    link: str | None = None


class TrainingFolderUpdate(BaseModel):
    name: str | None = None
    link: str | None = None


class TrainingFile(BaseModel):
    id: int
    folder_id: int | None = None
    name: str
    route: str | None = None


class TrainingFileCreate(BaseModel):
    folder_id: int | None = None
    name: str | None = None
    route: str | None = None


class ToDoCategory(BaseModel):
    id: int
    title: str

class ToDoCategoryCreate(BaseModel):
    title: str

class ToDoList(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    user_name: str
    category_id: int
    date: str


class ToDoListCreate(BaseModel):
    user_id: int
    title: str
    description: str
    user_name: str
    category_id: int


class ToDoListUpdate(BaseModel):
    user_id: int
    title: str
    description: str
    user_name: str
    category_id: int

