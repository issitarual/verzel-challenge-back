from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from db.db_setup import get_db
from schemas.user import UserCreate, User, UserUpdate
from crud.user import get_user, get_user_by_email, create_user, delete_user_by_id,update_user_by_id, get_all_users
from models.user import User as UserModel
from secutiry import get_password_hash

router = fastapi.APIRouter()


@router.post("/users", response_model=User, status_code=201)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.scalar(select(UserModel).where(UserModel.email == user.email))
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    hashed_password = get_password_hash(user.password)
    return create_user(db=db, user=user, hashed_password=hashed_password)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int,db: Session = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get('/users/', response_model=List[User])
async def read_users(db: Session = Depends(get_db)):
    return get_all_users(db=db)


@router.delete('/user/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user_by_id(db=db,user_id=user_id)
    return f"User {user_id} deleted successfully"


@router.patch("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = get_password_hash(user.password)
    db_user = update_user_by_id(db=db,user_id=user_id, user=user, hashed_password=hashed_password)

    return db_user