from fastapi import APIRouter,Depends,UploadFile,File
from sqlalchemy.ext.asyncio import AsyncSession
from utils.dbconnection import get_db
from doctors import services
from .models import docent,DoctorResponse


router=APIRouter(prefix="/doctor")


@router.get("/admin/all")
async def hex(dba:AsyncSession=Depends(get_db)):
    return await services.sab(dba)


@router.post("/login", response_model=DoctorResponse)
async def vex(data: docent, db: AsyncSession=Depends(get_db)):
    return await services.login(data,db)


@router.post("/signin")
async def rex(data: docent, dba: AsyncSession = Depends(get_db)):
   return await services.sin(data,dba)


@router.post("/upload/{i_d}")
async def dex(i_d:int,file:UploadFile=File(),dba:AsyncSession=Depends(get_db)):
    return await services.upld(i_d,file,dba)


    

