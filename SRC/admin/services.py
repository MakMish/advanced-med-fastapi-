from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from SRC.admin.models import xer
from fastapi import Form
from SRC.appointment.schemas import apttab
async def abc(dba : AsyncSession):
    data=await dba.execute(select(apttab))
    p=data.scalars().all()
    return{
        "data":p
    }

async def dce(dba:AsyncSession,m:xer=Form(...)):
    result=await dba.execute(select(apttab).where(apttab.datee1==m.dat4))
    v=result.scalars().all()
    if v is None:
        return{
            "status":"invalid date"
        }
    return v