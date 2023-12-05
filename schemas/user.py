from datetime import datetime
from typing import Optional, List
from models.order import Order
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    name: str
    isUserAdmin: bool


class User(UserBase):
    id: int
    name: str
    isUserAdmin: bool
    # created_at: datetime
    # updated_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: str=None
    # updated_at: datetime

    class Config:
        from_attributes = True