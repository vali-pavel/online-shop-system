from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os, time

from . import models

load_dotenv()

DATABASE_URI = f'mysql+pymysql://{os.environ["MYSQL_USER"]}:{os.environ["MYSQL_ROOT_PASSWORD"]}@users-db:3306/users'
engine = create_engine(DATABASE_URI)


def _get_engine_connection():
    conn = None
    counter = 3
    connection_ok = False
    while counter > 0 and not connection_ok:
        try:
            conn = engine.connect()
            connection_ok = True
            return conn
        except:
            counter = counter - 1
            time.sleep(7)
    if not connection_ok:
        raise Exception("Database connection failed")


def create_tables():
    models.Base.metadata.create_all(bind=conn)


def drop_tables():
    models.Base.metadata.drop_all(bind=conn)


conn = _get_engine_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conn)
create_tables()
