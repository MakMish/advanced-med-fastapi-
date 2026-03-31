from fastapi import HTTPException
from .schemas import doctab
import cloudinary
import cloudinary.uploader
from passlib.context import CryptContext
from utils.authenticutils import create_refresh_token


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
cloudinary.config(
    cloud_name = "dlnrhk4hj", 
    api_key = "696748244379315", 
    api_secret = "_eS3yKJk4RM3VBNXonMEMD7i7NI",
    secret=True
)


def sab(dba):
    data=dba.query(doctab).all()
    if data is None:
        return None
    return data




def login(data, db):

    doctor = db.query(doctab).filter(doctab.email == data.email).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    pwd_context.verify(data.password,doctor.password)




def sin(data, dba):
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

    dba.add(v)
    dba.commit()
    dba.refresh(v)

    return {
        "refresh_token": token
    }



def upld(i_d,file,dba):
    max_size=2*1024*1024
    if file.size> max_size:
        return{
            "file status": " file is too large"
        }
    result=cloudinary.uploader.upload(file.file)
    v=result.get("url")
    x=dba.query(doctab).filter(doctab.doc_id==i_d).first()
    if x is None:
        return{
            "status":"not a valid id"
        }
    x.img_url=v
    dba.commit()
    dba.refresh(v)
    return{
        "status":"success"
    }