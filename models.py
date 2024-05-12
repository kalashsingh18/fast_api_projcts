from database import base
from sqlalchemy import Column,String,INTEGER,Boolean,TIMESTAMP,ForeignKey,LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
class users(base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Post(base):
    __tablename__="post"
    id=Column(INTEGER,primary_key=True,nullable=False)
    content=Column(String,nullable=False)
    title=Column(String,nullable=False)
    image_data = Column(LargeBinary)
    published=Column(Boolean,nullable=False,server_default='True')
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    owner_id=Column(INTEGER,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner=relationship(users)
class vote(base):
   __tablename__="votes"
   post_id=Column(INTEGER,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)
   user_id=Column(INTEGER,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    