from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from datetime import datetime,timedelta
import models
import auth
from sqlalchemy.orm import Session
from database import get_db
from jose import jwt
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 6000000
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")
def create_acess_token(data:dict):
    to_encode=data.copy()
    expire_time=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire_time})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
def verify_the_token(token: str = Depends(auth.oauth2_scheme),db:Session =Depends(get_db)):
    payload=jwt.decode(token,auth.SECRET_KEY,algorithms=[auth.ALGORITHM])
    print("check:",payload)
    check=db.query(models.users).filter(models.users.user_name==payload["user_name"]).first()
    
    print("check:",check)
    checks=payload["user_pass"]==check.Password
    

    print(checks)
    if checks:
        return payload
    else:
        return {"message":"not authorized"}
def get_current_user(token:str =Depends(auth.oauth2_scheme),db:Session =Depends(get_db)):
    x=verify_the_token(token)
    return x
