from fastapi import APIRouter,Depends,UploadFile,File
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from utils.dbconnection import get_db
import services
from .models import data,urespmodel


router=APIRouter(prefix="user")


@router.get("/admin/all",response_model=list[urespmodel])
def hex(dba:Session=Depends(get_db)):
    return services.sab(dba)


@router.post("/login")
def vex(data:OAuth2PasswordRequestForm=Depends(),dba:Session=Depends(get_db)):
    return services.lin(data,dba)


@router.post("/signin")
def rex(data: data, dba: Session = Depends(get_db)):
    return services.sin(data,dba)


@router.post("/upload")
def dex(file:UploadFile=File()):
    return services.upld(file)
    


    