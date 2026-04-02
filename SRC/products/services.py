from SRC.products.schemas import tablepro
from SRC.products.models import data
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
async def xsz(db : AsyncSession):
    result=await db.execute(select(tablepro))
    v=result.scalars().all()
    if v is None:
            return{
                    "status":"no order"
            }
    db.commit()
    return{
        "products":v
    }
    
async def  cse(data,dba:AsyncSession):
            m=tablepro(
            product=data.product,
            description=data.description,
            availablity=data.availablity,
            img_url=data.img_url_1
                 )
            dba.add(m)
            await dba.commit()
            await dba.refresh(m)
            return{
                "status":"data added"
            }
async def cce(i_d:data,dba:AsyncSession):
       result=await dba.execute(select(tablepro).where(tablepro.order_id==i_d.i_d))
       x=result.scalars().first()
       await dba.delete(x)
       await dba.commit()
       return{
        "status":" product cancelled"
       }


