from fastapi import APIRouter,Depends
import schemas
from sqlalchemy.orm import Session
from database import get_db
import models
import utils
import auth
from jose import jwt
import auth
router_user=APIRouter(tags=["user"])
@router_user.post("/create_user")
def create_user(user:schemas.user_create,db:Session =Depends(get_db)):
    user.Password=utils.hash(user.Password)
    users=dict(user)
    user_detail= models.users(**users)
    db.add(user_detail)
    db.commit()
    token=auth.create_acess_token(data={"user_pass":user.Password,"user_name":user.user_name})
    return {"created":user.user_name,"token":token,"token_type": "bearer"}
@router_user.post("/sign_in")
def sign_in(data:schemas.usersign_in,db:Session =Depends(get_db)):
    
    checkuser=db.query(models.user).filter(models.user.user_name==data.user_name).first()
    constraints=utils.verify(data.Password,checkuser.Password)
    if constraints:
        token=auth.create_acess_token(data={"user_pass":data.Password,"user_name":data.user_name})
        return {"created":data.user_name,"token":token,"token_type": "bearer"}
@router_user.get("/get_info_user")
def getall(db:Session =Depends(get_db),data:dict =Depends(auth.verify_the_token)):
        user_data=db.query(models.users).all()
        return user_data

