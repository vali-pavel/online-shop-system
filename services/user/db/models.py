from sqlalchemy import Column, Integer, String

from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(Integer, nullable=False)
    role_type = Column(Integer, nullable=False)
    hashed_password = Column(String(100), nullable=False)
