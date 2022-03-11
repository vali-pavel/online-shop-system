from sqlalchemy import Table, Column, Integer, String
from db import meta

user = Table(
    "user",
    meta,
    Column("user_id", Integer, autoincrement=True, primary_key=True),
    Column("full_name", String(100), nullable=False),
    Column("email", String(100), nullable=False),
    Column("phone_number", Integer, nullable=False),
    Column("user_role", Integer, nullable=False),
    Column("password", String(150), nullable=False),
)
