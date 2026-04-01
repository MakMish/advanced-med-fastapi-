from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from appointment import services
from utils.dbconnection import get_db
from .models import aptent


router=APIRouter(prefix="/apt")

@router.get("/all")
async def hex(dba:AsyncSession=Depends(get_db)):
    return await services.abc(dba)



@router.get("/bydate")          #24-05-2946
async def vex(date:date,dba:AsyncSession=Depends(get_db)):
    return await services.sce(date,dba)
    
@router.post("/book")          #24-05-2946
async def rex(data:aptent,dba:AsyncSession=Depends(get_db)):
    return await services.scb(data,dba)


@router.delete("/cancel/{i_d}")          #24-05-2946
async def dex(i_d:int,dba:AsyncSession=Depends(get_db)):
    return await services.scd(i_d,dba)
   
    