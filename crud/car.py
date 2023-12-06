from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.car import Car
from schemas.car import CarCreate,CarUpdate

async def get_car(db: AsyncSession, car_id: int):
    query = select(Car).where(Car.id == car_id)
    result = db.execute(query)
    return result.scalar_one_or_none()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Car).offset(skip).limit(limit).all()


def get_car_by_model(db: Session, model: str):
    return db.query(Car).filter(Car.model == model).first()


def create_car(db: Session, car: CarCreate):
    db_car = Car(model=car.model, brand=car.brand, price=car.price, image=car.image)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def delete_car_by_id(db: Session, car_id: int):
    query = db.query(Car).get(car_id)
    db.delete(query)
    db.commit()
    db.close()
    return None


def update_car_by_id(db:Session,car_id,car: CarUpdate):
    db_car = db.query(Car).get(car_id)
    car_data = car.dict(exclude_unset=True)
    for key, value in car_data.items():
        setattr(db_car, key, value)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    db.close()
    return db_car