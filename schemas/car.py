from typing import Optional, List
from pydantic import BaseModel


class CarBase(BaseModel):
    model: str
    brand: str
    price: str
    image: str


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    # created_at: datetime
    # updated_at: datetime

    class Config:
        from_attributes = True

class CarUpdate(BaseModel):
    model: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[str] = None
    image: Optional[str] = None
    # updated_at: datetime

    class Config:
        from_attributes = True