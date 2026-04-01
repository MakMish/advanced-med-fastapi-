from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from utils.dbconnection import get_db
from .models import xer
from admin import services

routes2=APIRouter(
    prefix="/history"
)


@routes2.get("/order_all")
async def hex(dba:AsyncSession=Depends(get_db)):
    return await services.abc(dba)
    


@routes2.get("/order")
async def rex(m:xer,dba:AsyncSession=Depends(get_db)):
    return await services.dce(m,dba)
    