from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
import pytz
from sqlalchemy import select
from doctors.schemas import doctab
SECRET_KEY = "mymedapp"
ALGORITHM = "HS256"
EXP_TIME_ACCESSTOKEN_MIN = 15
EXP_TIME_REFRESHTOKEN_DAYS = 1
# 🔹 CREATE REFRESH TOKEN
def create_refresh_token(data: dict):
    try:
        to_encode = data.copy()
        expire = datetime.now(pytz.timezone("Asia/Kolkata")) + timedelta(days=EXP_TIME_REFRESHTOKEN_DAYS)
        to_encode.update({"exp": expire})

        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return token 

    except JWTError:
        return None


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
        expire = datetime.now() + timedelta(minutes=EXP_TIME_ACCESSTOKEN_MIN)
        to_encode.update({"exp": expire})

        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return token

    except JWTError:
        return None
    

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
        return {"status": "expired or invalid refresh token"}


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
        return {"status": "expired or invalid access token"}