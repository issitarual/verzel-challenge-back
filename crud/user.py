from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.user import User
from schemas.user import UserCreate,UserUpdate, UserBase

async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = db.execute(query)
    return result.scalar_one_or_none()

def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_email(db: Session, user: UserBase):
    return db.scalar(select(User).where(User.email == user.email))


def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(email=user.email, password=hashed_password, name=user.name, isUserAdmin=user.isUserAdmin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    query = db.query(User).get(user_id)
    db.delete(query)
    db.commit()
    db.close()
    return None


def update_user_by_id(db:Session,user_id,user: UserUpdate,hashed_password: str):
    db_user = db.query(User).get(user_id)
    db_user.password = hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user