from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
database_url="postgresql+psycopg2://overall_9lwr_user:wUGhzah8DXIVrzZ8IhYJ8vMylJ7JTbn9@dpg-cp9o6sn109ks73ac86tg-a.oregon-postgres.render.com/overall_9lwr"
engine=create_engine(database_url)
session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)
base=declarative_base()
def get_db():
    db =session_local()
    try:
        yield db
    finally:
        db.close()