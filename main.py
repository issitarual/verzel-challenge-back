from fastapi import FastAPI

from api import cars, users, orders
from db.db_setup import engine
from models import user, car, order
from fastapi.middleware.cors import CORSMiddleware

user.Base.metadata.create_all(bind=engine)
car.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(cars.router)
app.include_router(orders.router)