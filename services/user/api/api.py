from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, APIRouter

from db.db import SessionLocal
from . import schemas, db_manager
from user import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.UserCreate)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = User(db)
    created_user = user.createUser(user_in)
    if created_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")

    auth_token = user.get_auth_token(created_user.id, created_user.role_type)
    return Response(headers={"authorization": auth_token}, status_code=201)


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db_manager.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/login")
def user_login(user_in: schemas.UserLogin, db: Session = Depends(get_db)):
    user = User(db)
    db_user = user.login(user_in)
    if not db_user:
        raise HTTPException(status_code=401, detail="Wrong email or password")
    auth_token = user.get_auth_token(db_user.id, db_user.role_type)
    return Response(headers={"authorization": auth_token}, status_code=200)
