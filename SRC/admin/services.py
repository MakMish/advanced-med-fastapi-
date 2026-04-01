from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import tablerec
async def abc(dba : AsyncSession):
    data=await dba.execute(select(tablerec))
    p=data.scalars().all()
    return{
        "data":p
    }

async def dce(m,dba:AsyncSession):
    result=await dba.execute(select(tablerec).where(tablerec.date==m))
    v=result.scalars().all()
    if v is None:
        return{
            "status":"invalid date"
        }
    return v