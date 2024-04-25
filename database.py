from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
database_url="postgresql+psycopg2://ems_api_database_user:yfWBbypt3Grdl2dXLH3G3hwJaIAQhKkR@dpg-col8sdgcmk4c73bnvq3g-a.oregon-postgres.render.com/ems_api_database"
engine=create_engine(database_url)
session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)
base=declarative_base()
def get_db():
    db =session_local()
    try:
        yield db
    finally:
        db.close()