from fastapi import APIRouter,Depends,Form
from sqlalchemy.ext.asyncio import AsyncSession
from SRC.utils.dbconnection import get_db
from SRC.admin.models import xer
from SRC.admin import services

routes2=APIRouter(
    prefix="/history"
)


@routes2.get("/order_all")
async def hex(dba:AsyncSession=Depends(get_db)):
    return await services.abc(dba)
    


@routes2.get("/order")
async def rex(m:xer=Form(...),dba:AsyncSession=Depends(get_db)):
    return await services.dce(dba,m)
    