from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.db_setup import Base

class Order(Base):

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer)
    user_id = Column(Integer)
    # created_at = Column(DateTime(timezone=True), server_default=func.now())