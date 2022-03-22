from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, nullable=False)
    sku = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    color = Column(String(50), nullable=False)
    inventory = Column(Integer, nullable=False)
    min_delivery_days = Column(Integer, nullable=False)
    max_delivery_days = Column(Integer, nullable=False)
    vendor_name = Column(String(200), nullable=False)
    category = Column(Integer, nullable=False)
