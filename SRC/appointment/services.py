from .schemas import apttab
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
async def abc(dba:AsyncSession):
    result=await dba.execute(select(apttab))
    v=result.scalars().all()
    return v

async def sce(date,dba:AsyncSession):
    result=await dba.execute(select(apttab).where(apttab.datee1==date))
    v=result.scalars().all()
    if v is None:
        return{
            "status":"no apt on this date"
        }
    return v

async def scb(data,dba:AsyncSession):
    v=apttab(
             doc_name=data.doc_name,
             client_name=data.client_name,
             client_mob=data.client_mob,
             time_slot=data.slot,
             datee1=data.da1
            )
    await dba.add(v)
    await dba.commit()
    await dba.refresh(v)
    return{
        "status": " appointment booked"
    }

async def scd(i_d,dba:AsyncSession):
    result=await dba.execute(select(apttab).where(apttab.client_id==i_d))
    v=result.scalars().first()
    dba.delete(v)
    dba.commit()
    dba.refresh(v)
    if v is None:
        return {
            "status":" not any apt"
        }



