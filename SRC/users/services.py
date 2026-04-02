from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import user_table
import cloudinary
from sqlalchemy import select
import cloudinary.uploader
from passlib.context import CryptContext
from utils.user_authenticutils import create_refresh_token
from .models import data
from model import setting
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
mk=setting()
cloudinary.config(
    cloud_name=mk.cloud_name, 
    api_key=mk.api_key, 
    api_secret=mk.api_secret,
    secret=True
)

async def sab(dba:AsyncSession):
    result=await dba.execute(select(user_table))
    data=result.scalars().all()
    if data is None:
        return None
    return  data

async def sin(user_data: data, dba: AsyncSession):
    token = create_refresh_token({"email": user_data.uemail})

    user = user_table(
        uname=user_data.username,
        uemail=user_data.uemail,
        hash_upassword=pwd_context.hash(user_data.password),
        umobile=user_data.umobile,
        uaddress=user_data.uaddress,
        ref_token=token
    )

    dba.add(user)
    await dba.commit()
    await dba.refresh(user)

    return {"refresh_token": token}

async def sin(data: data, dba: AsyncSession):
    token = create_refresh_token({
        "email": data.uemail
    })
    data=user_table(
        uname=data.username,
        uemail=data.uemail,
        hash_upassword=pwd_context.hash(data.password),
        umobile=data.umobile,
        uaddress=data.uaddress,
        ref_token=token
    )
    dba.add(data)
    await dba.commit()
    await dba.refresh(data)

    return {
        "refresh_token": token
    }


async def upld(file):
    max_size=2*1024*1024
    content=await file.read()
    if len(content)> max_size:
        return{
            "file status": " file is too large"
        }
    result=await cloudinary.uploader.upload(file.file)
    return{
        "sec_url": result["secure_url"],
        "url": result.get("url")
    }

