from datetime import datetime
from typing import Optional, List
from models.order import Order
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str
    isUserAdmin: bool


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    password: str
    # created_at: datetime
    # updated_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    paassword: str=None
    # updated_at: datetime

    class Config:
        from_attributes = True