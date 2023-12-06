from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from schemas.order import OrderCreate, Order
from crud.order import create_order, get_orders_by_user

router = fastapi.APIRouter()


@router.post("/order", response_model=Order, status_code=201)
async def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)


@router.get("/order/{user_id}", response_model=List[Order])
async def read_user_order(user_id: int, db: Session = Depends(get_db)):
    orders = await get_orders_by_user(user_id=user_id, db=db)
    return orders