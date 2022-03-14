from sqlalchemy import Column, Integer, String, Date

from .db import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    shipping_address = Column(String(250))
    billing_address = Column(String(250))
    card_number = Column(Integer)
    card_expiration = Column(Date)
    card_holder = Column(String(100))
