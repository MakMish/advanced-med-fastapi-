from jose import jwt, JWTError
from fastapi import HTTPException
from datetime import datetime, timedelta,timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from model import setting
from doctors.schemas import doctab
SECRET_KEY = setting().SECRET_KEY
ALGORITHM = setting().ALGORITHM
EXP_TIME_ACCESSTOKEN_MIN = 15
EXP_TIME_REFRESHTOKEN_DAYS = 1
# 🔹 CREATE REFRESH TOKEN
def create_refresh_token(data: dict):
    try:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=EXP_TIME_REFRESHTOKEN_DAYS)
        to_encode.update({"exp": expire})

        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return token 

    except JWTError:
        raise HTTPException(status_code=404,detail="teoken expired")

# 🔹 CREATE ACCESS TOKEN
async def create_access_token(reftok: str, dba: AsyncSession):
    try:
        payload=jwt.decode(reftok,SECRET_KEY,algorithms=ALGORITHM)
        result = await dba.execute(select(doctab).where(doctab.name==payload.get("email")))
        user=result.scalars().first()
        if user is None:
            return {"status": "invalid refresh token"}

        data = {"email": user.uemail}
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=EXP_TIME_ACCESSTOKEN_MIN)
        to_encode.update({"exp": expire})

        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return token

    except JWTError:
        raise HTTPException(status_code=404,detail="teoken expired")

# 🔹 VERIFY REFRESH TOKEN
async def verify_reftok(reftok: str, dba: AsyncSession):
    try:
        payload = jwt.decode(reftok, SECRET_KEY, algorithms=[ALGORITHM])
        result = await dba.execute(select(doctab).where(doctab.name==payload.get("email")))
        user=result.scalars().first()
        if user is None:
            return {"status": "invalid user"}

        return {"status": "valid refresh token"}

    except JWTError:
       raise HTTPException(status_code=404,detail="teoken expired")


# 🔹 VERIFY ACCESS TOKEN
async def verify_acctok(acctok: str, dba: AsyncSession):
    try:
        payload = jwt.decode(acctok, SECRET_KEY, algorithms=[ALGORITHM])

        email = payload.get("email")

        result = await dba.execute(select(doctab).where(doctab.name==payload.get("email")))
        user=result.scalars().first()
        if user is None:
            return {"status": "user not found"}

        return {"status": "logged in"}

    except JWTError:
        raise HTTPException(status_code=404,detail="teoken expired")
    
async def logout(reftok:str,dba:AsyncSession):
    try:
        result=await dba.execute(select(doctab).where(doctab.ref_token==reftok))
        user=result.scalars().first()
        if user is None:
            raise HTTPException(status_code=405,detail="user isn't exists")
        await dba.delete(user)
        await dba.commit()
        await dba.refresh(user)
    except:
        raise HTTPException(status_code=404,detail="internal error")