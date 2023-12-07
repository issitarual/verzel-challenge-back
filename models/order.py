from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.db_setup import Base
from sqlalchemy.orm import Mapped

class Order(Base):

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    qtd = Column(Integer)
    car_id = Column(Integer, ForeignKey("cars.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    # created_at = Column(DateTime(timezone=True), server_default=func.now())

    cars: Mapped["Car"] = relationship()