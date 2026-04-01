from fastapi import APIRouter,Depends,UploadFile,File
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from utils.dbconnection import get_db
import users.services
from .models import data,urespmodel


router=APIRouter(prefix="/user")


@router.get("/admin/all",response_model=list[urespmodel])
async def hex(dba:AsyncSession=Depends(get_db)):
    return await users.services.sab(dba)


@router.post("/login")
async def vex(data:OAuth2PasswordRequestForm=Depends(),dba:AsyncSession=Depends(get_db)):
     return await users.services.lin(data,dba)


@router.post("/signin")
async def rex(data: data, dba: AsyncSession = Depends(get_db)):
    return await users.services.sin(data,dba)


@router.post("/upload")
async def dex(file:UploadFile=File(...)):
    return await users.services.upld(file)
    


    