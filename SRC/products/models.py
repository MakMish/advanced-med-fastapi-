from pydantic import BaseModel

class tabent1(BaseModel):
    product:str
    description:str
    availablity:bool
    