from typing import List
from pydantic import BaseModel

class OrderBase(BaseModel):
    car_id: int
    user_id: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    # created_at: datetime

    class Config:
        from_attributes = True


class Config:
        from_attributes = True