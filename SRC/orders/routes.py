from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from SRC.utils.dbconnection import get_db 
from SRC.orders import services
from SRC.orders.models import tabent,data
router=APIRouter(prefix="/orders")

@router.get("/all")
async def hex(dba:AsyncSession=Depends(get_db)):
       return await services.xsz(dba)
    
@router.post("/give",status_code=201)
async def vex(data:tabent, dba:AsyncSession=Depends(get_db)):
      return await services.cse(data,dba)

@router.delete("/cancel")
async def rex(i_d:data,dba:AsyncSession=Depends(get_db)):
        return await services.cce(i_d,dba)
          
