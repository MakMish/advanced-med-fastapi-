from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from utils.dbconnection import get_db
from .models import tabent1
from products import services
router=APIRouter(prefix="/products")

@router.get("/all")
async def hex(dba:AsyncSession=Depends(get_db)):
        return await services.xsz(dba)    
@router.post("/give",status_code=201)
async def  vex(data:tabent1,dba:AsyncSession=Depends(get_db)):
        return await services.cse(data,dba)

@router.delete("/cancel")
async def rex(i_d:int,dba:AsyncSession=Depends(get_db)):
        return await services.cce(i_d,dba)

