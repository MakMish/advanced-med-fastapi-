from fastapi import APIRouter,Depends,UploadFile,File
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from SRC.utils.dbconnection import get_db
from SRC.users import services
from SRC.users.models import data,urespmodel


router=APIRouter(prefix="/user")


@router.get("/admin/all",response_model=list[urespmodel])
async def hex(dba:AsyncSession=Depends(get_db)):
    return await services.sab(dba)


@router.post("/login")
async def vex(data:OAuth2PasswordRequestForm=Depends(),dba:AsyncSession=Depends(get_db)):
     return await services.lin(data,dba)


@router.post("/signin")
async def rex(data: data, dba: AsyncSession = Depends(get_db)):
    return await services.sin(data,dba)


@router.post("/upload")
async def dex(file:UploadFile=File(...)):
    return await services.upld(file)
    


    