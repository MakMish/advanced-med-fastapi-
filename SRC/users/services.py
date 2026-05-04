from sqlalchemy.ext.asyncio import AsyncSession
from SRC.users.schemas import user_table
from fastapi import UploadFile,File
import cloudinary
from sqlalchemy import select
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import cloudinary.uploader
from passlib.context import CryptContext
from SRC.utils.user_authenticutils import create_refresh_token
from SRC.users.models import data
from SRC.model import setting
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
mak=setting()
cloudinary.config( 
    cloud_name=mak.cloud_name, 
    api_key=mak.api_key, 
    api_secret=mak.api_secret,
    secure = True
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

    return {"refresh_token": token,
            "status":"ci/cd working 2223333"
            }

async def lin(data:OAuth2PasswordRequestForm, dba: AsyncSession):
        result=await dba.execute(select(user_table).offset(5).limit(5))
        value=result.scalars().first()
        if value is None:
            raise HTTPException(status_code=402,detail="user isn't exists")
        x=pwd_context.verify(data.password,value.hash_upassword)

        if x==False:
             raise HTTPException(status_code=404,detail="false password")
        else:
             return{
                  "status":"logged in"
             }

async def upld(file:UploadFile=File(...)):
         if file is None:
              return {
                   "file":"empty"
              }
         max_size=2*1024*1024
        #  content=await file.read()
         if file.size > max_size:
              raise HTTPException(status_code=488,detail="file is latrge")
         result=cloudinary.uploader.upload(file.file)
         return{
        "sec_url": result["secure_url"],
        "url": result.get("url")
            }


