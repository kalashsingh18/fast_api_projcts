from pydantic import BaseModel,EmailStr
class user_create(BaseModel):
    user_name:str
    email:EmailStr
    Password:str
class usersign_in(BaseModel):
    user_name:str
    Password:str
class Post(BaseModel):
    content:str
    title:str
class update_post_title(BaseModel):
    
    title:str
class update_post_content(BaseModel):
    content:str
class update_user_username(BaseModel):
    user_name:str
class update_user_email(BaseModel):
    email:EmailStr
class votes(BaseModel):
    post_id: int 
    dir :int
class post_out(BaseModel):
    post:dict
    votes:int
    
    
    
    