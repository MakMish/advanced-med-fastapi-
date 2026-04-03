from fastapi import APIRouter,Depends,UploadFile,File,Form
from sqlalchemy.ext.asyncio import AsyncSession
from SRC.utils.dbconnection import get_db
from SRC.doctors import services
from SRC.doctors.models import DoctorResponse
from SRC.doctors.models import docent
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(prefix="/doctor")


@router.get("/admin/all",response_model=list[DoctorResponse])
async def hex(dba:AsyncSession=Depends(get_db)):
    return await services.sab(dba)


@router.post("/login")
async def vex(data:OAuth2PasswordRequestForm=Depends(), db: AsyncSession=Depends(get_db)):
    return await services.login(data,db)


@router.post("/signin")
async def rex(data: docent, dba: AsyncSession = Depends(get_db)):
   return await services.sin(data,dba)


@router.post("/upload")
async def dex(i_d:int=Form(...),file:UploadFile=File(),dba:AsyncSession=Depends(get_db)):
    return await services.upld(dba,i_d,file)


    

