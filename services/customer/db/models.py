from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    shipping_address = Column(String(250))
    billing_address = Column(String(250))
    card_number = Column(String(50))
    card_expiration = Column(String(50))
    card_holder = Column(String(100))
