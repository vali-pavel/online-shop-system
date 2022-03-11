from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = f'mysql+pymysql://{os.environ["MYSQL_USER"]}:{os.environ["MYSQL_PASS"]}@localhost:3306/users'

meta = MetaData()
engine = create_engine(DATABASE_URI)
conn = engine.connect()
