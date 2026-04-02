from pydantic import BaseModel

class tabent1(BaseModel):
    product:str
    description:str
    availablity:bool
    img_url_1:str

class data(BaseModel):
    i_d:int
    