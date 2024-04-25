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
    
    