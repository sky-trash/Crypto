from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from db.database import engine
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Annotated
from db import models, schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(login: str, password: str, db: Session):
    user = db.query(models.User).where(models.User.login == login).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="permission denied",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("login")
        role: schemas.Role = payload.get("role")
        if login is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=login)
    except JWTError:
        raise credentials_exception
    user = Session(bind=engine).query(models.User).filter(models.User.login == login).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_admin(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    admin_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="permission denied",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("login")
        role: schemas.Role = payload.get("role")
        if login is None:
            raise credentials_exception
        if role not in ['ROLE_ADMIN']:
            raise admin_exception
        token_data = schemas.TokenData(username=login)
    except JWTError:
        raise credentials_exception
    user = Session(bind=engine).query(models.User).filter(models.User.login == login).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[schemas.User, Depends(get_current_user)]
):
    return current_user


async def get_current_active_admin(
        current_user: Annotated[schemas.User, Depends(get_current_admin)]
):
    return current_user


async def token(form_data, db):
    user = authenticate_user(login=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"login": user.login, "role": user.role.title}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
