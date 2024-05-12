from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import schemas
import auth
from database import get_db
import schemas
from sqlalchemy import func
import models
from database import get_db
router_post=APIRouter(tags=["post_APIS"])
@router_post.post("/create_post")
def create_post(post:schemas.Post,db:Session=Depends(get_db),data:dict =Depends(auth.verify_the_token)):
    print("data",dict(data))
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
    print(data)
    check=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
    posts=db.query(models.Post).filter(models.Post.owner_id==check.id).all()
    response=[]
    for  i in posts:
                        vote_count = db.query(func.count(models.vote.post_id)) \
                           .filter(models.vote.post_id == i.id) \
                           .scalar()
                        i={"content":i.content,"title":i.title ,"id":i.id}
                        res=schemas.post_out(post=i,votes=vote_count)
                        response.append(res)
                        
    return response
    return posts
@router_post.delete("/delete_post")
def delete_post(db:Session=Depends(get_db),data:dict =Depends(auth.verify_the_token)):
    check=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
    print(check)
    posts=db.query(models.Post).filter(models.Post.owner_id==check.id)
    posts.delete(synchronize_session=False)
    db.commit()
    return {"message":"deleted"}
    
        


