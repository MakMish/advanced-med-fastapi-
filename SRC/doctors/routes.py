from fastapi import APIRouter,Depends,UploadFile,File
from sqlalchemy.orm import Session
from utils.dbconnection import get_db
import services
from .models import docent,DoctorResponse


router=APIRouter(prefix="/doctor")


@router.get("/admin/all")
def hex(dba:Session=Depends(get_db)):
    return services.sab(dba)


@router.post("/login", response_model=DoctorResponse)
def vex(data: docent, db: Session=Depends(get_db)):
    return services.login(data,db)


@router.post("/signin")
def rex(data: docent, dba: Session = Depends(get_db)):
   return services.sin(data,dba)


@router.post("/upload/{i_d}")
def dex(i_d:int,file:UploadFile=File(),dba:Session=Depends(get_db)):
    return services.upld(i_d,file,dba)


    

