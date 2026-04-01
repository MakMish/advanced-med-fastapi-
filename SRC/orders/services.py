from .schemas import table1  
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
async def xsz(dba:AsyncSession):
    result=await dba.execute(select(table1))
    v=result.scalars().all()
    dba.commit()
    return{
        "orders":v
    }


async def  cse(data, dba:AsyncSession):
            m=table1(
            product=data.product,
            quantity=data.quantity
                 )
            await dba.add(m)
            await dba.commit()
            await dba.refresh(m)
            return{
                "status":"data added"
            }

async def cce(i_d,dba:AsyncSession):
       result=await dba.execute(select(table1).where(table1.order_id==i_d))
       x=result.scalars().first()
       await dba.delete(x)
       await dba.commit()
       await dba.refresh(x)
       return{
        "status":" order cancelled"
       }