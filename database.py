from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url="postgresql+psycopg2://ems_api_database_p0cy_user:xXVXa3z4Zu9x2dh0dAuyZDkWqQ3nBgzv@dpg-cp0hngg21fec73855e9g-a/ems_api_database_p0cy"
engine=create_engine(database_url)
session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)
base=declarative_base()
def get_db():
    db =session_local()
    try:
        yield db
    finally:
        db.close()