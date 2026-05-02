from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base
from SRC.model import setting
mas=setting()
engine=create_async_engine(mas.url,
                           pool_size=10,
                           max_overflow=20,
                           pool_recycle=1800,
                           pool_timeout=60
                        )
Base=declarative_base()
localsession=sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
async def  get_db():
    db=localsession()
    try:
        yield db
    finally:
        await db.close() 

