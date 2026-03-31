from pydantic import BaseModel,EmailStr
class docent(BaseModel):
    name:str
    proffession:str
    email:EmailStr
    emg_mob:str
    hospital_name:str
    password:str
class DoctorResponse(BaseModel):
    doc_id: int
    name: str
    email: str
    proffession: str
    hospital_name: str
    img_url: str

    class Config:
        from_attributes = True   # (Pydantic v2)