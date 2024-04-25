from fastapi import FastAPI
from database import get_db,engine
from  routers.user import router_user
from routers.post import router_post
import models
app=FastAPI()

get_db()
models.base.metadata.create_all(bind=engine)
app.include_router(router_user)
app.include_router(router_post)
print("connected")
