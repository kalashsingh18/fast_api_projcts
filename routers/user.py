from fastapi import APIRouter,Depends
import schemas
from sqlalchemy.orm import Session
from database import get_db
import models
import utils
import auth
from sqlalchemy import func
from jose import jwt
import auth
import smtplib
from email.mime.text import MIMEText
import os
SENGRID_API_KEY=os.environ.get("SENDGRID_API_KEY") 
router_user=APIRouter(tags=["user"])
@router_user.post("/create_user")      
def create_user(user:schemas.user_create,db:Session =Depends(get_db)):
    
    user.Password=utils.hash(user.Password)
    users=dict(user)
    user_detail= models.users(**users)
    
    db.add(user_detail)
    db.commit()
    token=auth.create_acess_token(data={"user_pass":user.Password,"user_name":user.user_name})
    data={"gmail":user.email,
"subject":"congrats!",
"body_of_email":"your acount has been created"}
    send_email(data)
    return {"created":user.user_name,"token":token,"token_type": "bearer"}
@router_user.post("/sign_in")
def sign_in(data:schemas.usersign_in,db:Session =Depends(get_db)):
    
    checkuser=db.query(models.users).filter(models.users.user_name==data.user_name).first()
    constraints=utils.verify(data.Password,checkuser.Password)
    if constraints:
        token=auth.create_acess_token(data={"user_pass":data.Password,"user_name":data.user_name})
        return {"created":data.user_name,"token":token,"token_type": "bearer"}
@router_user.get("/get_info_user")
def getall(db:Session =Depends(get_db),data:dict =Depends(auth.verify_the_token)):
        user_data=db.query(models.users).all()
        return user_data
@router_user.put("/update_user_name")
def update_user(upn:schemas.update_user_username,db:Session =Depends(get_db),data:dict=Depends(auth.verify_the_token)):
    if data["user_name"]:
    
        user_details=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
        user_details.user_name=upn.user_name
        db.commit()
        return {"message":"updated"}
    else:
        return data
@router_user.put("/update_user_email")
def update_user(upn:schemas.update_user_email,db:Session =Depends(get_db),data:dict=Depends(auth.verify_the_token)):
    if data["user_name"]:
    
        user_details=db.query(models.users).filter(models.users.user_name==data["user_name"]).first()
        user_details.email=upn.email
        db.commit()
        return {"message":"updated"}
    else:
        return data
@router_user.post("/send_email")
def send_email(data:dict):
    print(data)
    
# Replace with your Gmail email address and password
    sender_gmail = 'kalashchouhan939@gmail.com'
    gmail_app_password = 'ogls exce mldi eszz'  # Use your regular Gmail password

# Create the email
    from_address = data["gmail"]
    to_address = sender_gmail
    subject = data["subject"]
    body = data["body_of_email"]

# Create a MIMEText object to represent the email
    msg = MIMEText(body)
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

# Connect to the Gmail SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_gmail, gmail_app_password)  # Log in with your Gmail password
        server.sendmail(from_address, [to_address], msg.as_string())

    print('Email sent successfully.')

          
      

