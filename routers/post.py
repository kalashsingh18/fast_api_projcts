from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import schemas
import auth
from database import get_db
import schemas
import models
from database import get_db
router_post=APIRouter()
@router_post.post("/create_post")
def create_post(post:schemas.Post,db:Session=Depends(get_db),data:dict =Depends(auth.verify_the_token)):
    user_data=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
    
    post=dict(post)
    post["owner_id"]=user_data.id
    post=models.Post(**post)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
@router_post.get("/get_all_post")#response_model=[schemas.Post])
def get_all_post(db:Session=Depends(get_db),data:dict =Depends(auth.verify_the_token)):
    check=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
    posts=db.query(models.Post).filter(models.Post.owner_id==check.id).all()
    return posts
@router_post.delete("/delete_post")
def delete_post(db:Session=Depends(get_db),data:dict =Depends(auth.verify_the_token)):
    check=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
    print(check)
    posts=db.query(models.Post).filter(models.Post.owner_id==check.id)
    posts.delete(synchronize_session=False)
    db.commit()
    return {"message":"deleted"}
    
        


