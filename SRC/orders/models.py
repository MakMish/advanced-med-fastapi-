from pydantic import BaseModel

class tabent(BaseModel):
    product:str
    quantity:int
    uaddress:str
class data(BaseModel):
    id:int
