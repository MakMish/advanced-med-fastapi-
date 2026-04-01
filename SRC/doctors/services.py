from fastapi import HTTPException
from .schemas import doctab
import cloudinary
import cloudinary.uploader
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from model import setting
from utils.authenticutils import create_refresh_token
from sqlalchemy import select
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
cloudinary.config(
    cloud_name = setting().cloud_name, 
    api_key = setting().api_key, 
    api_secret =setting().api_secret,
    secret=True
)


async def sab(dba : AsyncSession):
    result=await dba.execute(select(doctab))
    data=result.scalars().all()
    if data is None:
        return None
    return data




async def login(data, db : AsyncSession):
    result=await db.execute(select(doctab).where(doctab.email==data.email))
    doctor =result.scalars().first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    pwd_context.verify(data.password,doctor.password)
    return{
        "status":"logged in"
    }

async def sin(data, dba:AsyncSession):
    token = create_refresh_token({
        "email": data.uemail
    })
    ps=pwd_context.hash(data.password)

    v = doctab(
        name=data.name,
        proffession=data.proffession,
        emg_cont=data.emg_mob,
        email=data.email,
        hospital_name=data.hospital_name,
        ref_token=token,
        password=ps
    )

    await dba.add(v)
    await dba.commit()
    await dba.refresh(v)

    return {
        "refresh_token": token
    }



async def upld(i_d,file,dba:AsyncSession):
    max_size=2*1024*1024
    if file.size> max_size:
        return{
            "file status": " file is too large"
        }
    result=cloudinary.uploader.upload(file.file)
    v=result.get("url")
    data= await dba.execute(select(doctab).where(doctab.doc_id==i_d))
    x=data.scalars().first()
    if x is None:
        return{
            "status":"not a valid id"
        }
    x.img_url=v
    await dba.commit()
    await dba.refresh(v)
    return{
        "status":"success"
    }