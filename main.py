from fastapi import FastAPI

from api import cars, users, orders
from db.db_setup import engine
from models import user, car, order

user.Base.metadata.create_all(bind=engine)
car.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(cars.router)
app.include_router(orders.router)