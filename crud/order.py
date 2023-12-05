from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.order import Order
from schemas.order import OrderCreate


async def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).first().all()


def create_order(db: Session, order: Order):
    db_order = Order(user_id=order.user_id, car_id=order.car_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order