from pydantic import BaseModel,EmailStr
class data(BaseModel):
    username:str
    uemail:str
    password:str
    umobile:int
    uaddress:str

class usermodellogin(BaseModel):
    email:str
    password:str
class urespmodel(BaseModel):
    uname:str
    uemail:EmailStr
    umobile:int
    uaddress:str
    class config:
        from_attributes=True

