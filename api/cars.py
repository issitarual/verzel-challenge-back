from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from schemas.car import CarCreate, Car, CarUpdate
from crud.car import get_car, get_cars, get_car_by_model, create_car, delete_car_by_id,update_car_by_id

router = fastapi.APIRouter()


@router.get("/car", response_model=List[Car])
async def read_cars(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
):
    cars = get_cars(db, skip=skip, limit=limit)
    return cars


@router.post("/car", response_model=Car, status_code=201)
async def create_new_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = get_car_by_model(db=db, model=car.model)
    if db_car:
        raise HTTPException(
            status_code=400, detail="Model is already registered"
        )
    return create_car(db=db, car=car)


@router.get("/car/{car_id}", response_model=Car)
async def read_car(car_id: int,db: Session = Depends(get_db)):
    db_car = await get_car(db=db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car


@router.delete('/car/{car_id}')
async def delete_user(car_id: int, db: Session = Depends(get_db)):
    db_car = await get_car(db=db, car_id=car_id)
    print(db_car)
    if db_car is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_car_by_id(db=db,car_id=car_id)
    return f"User {car_id} deleted successfully"


@router.patch("/car/{car_id}", response_model=Car)
async def update_user(car_id: int, car: CarUpdate, db: Session = Depends(get_db)):
    db_car = await get_car(db=db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    db_car = update_car_by_id(db=db,car_id=car_id, car=car)
    return db_car