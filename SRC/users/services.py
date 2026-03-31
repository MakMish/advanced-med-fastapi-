from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from utils.dbconnection import get_db,engine,Base
from .schemas import user_table
import cloudinary
import cloudinary.uploader
from passlib.context import CryptContext
from utils.authenticutils import create_refresh_token
from .models import data,urespmodel
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
cloudinary.config(
    cloud_name = "dlnrhk4hj", 
    api_key = "696748244379315", 
    api_secret = "_eS3yKJk4RM3VBNXonMEMD7i7NI",
    secret=True
)

def sab(dba:Session=Depends(get_db)):
    data=dba.query(user_table).all()
    if data is None:
        return None
    return data

def lin(data:OAuth2PasswordRequestForm=Depends(),dba:Session=Depends(get_db)):
    og=dba.query(user_table).filter(user_table.uemail==data.username).first()
    if og is None:
        return{
            "status":"you need to signin"
        }
    x=pwd_context.verify(data.password,og.hash_upassword)
    if x==True:
        return{
            "hurray":"youn logged in boy"
        }
    return {
        "sorry": " your password is incorrect"
    }

def sin(data: data, dba: Session = Depends(get_db)):
    token = create_refresh_token({
        "email": data.uemail
    })

    v = user_table(
        uname=data.username,
        uemail=data.uemail,
        umobile=str(data.umobile),
        uaddress=data.uaddress,
        hash_upassword=pwd_context.hash(data.password),
        ref_token=token
    )

    dba.add(v)
    dba.commit()
    dba.refresh(v)

    return {
        "refresh_token": token
    }

def upld(file):
    max_size=2*1024*1024
    if file.size> max_size:
        return{
            "file status": " file is too large"
        }
    result=cloudinary.uploader.upload(file.file)
    return{
        "sec_url": result["secure_url"],
        "url": result.get("url")
    }

