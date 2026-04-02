from SRC.orders.schemas import table1  
from fastapi import HTTPException
from SRC.orders.models import data
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
async def xsz(dba:AsyncSession):
    result=await dba.execute(select(table1))
    v=result.scalars().all()
    dba.commit()
    return{
        "orders":v
    }


async def  cse(data1, dba:AsyncSession):
            m=table1(
            product=data1.product,
            quantity=data1.quantity,
            uaddress=data1.uaddress
                 )
            dba.add(m)
            await dba.commit()
            await dba.refresh(m)
            return{
                "status":"data added"
            }

async def cce(i_d:data,dba:AsyncSession):
       result=await dba.execute(select(table1).where(table1.order_id==i_d.id))
       x=result.scalars().first()
       if x is None:
               raise HTTPException(status_code=416,detail="order not found")
       await dba.delete(x)
       await dba.commit()
       return{
        "status":" order cancelled"
       }