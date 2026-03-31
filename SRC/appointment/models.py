from pydantic import BaseModel
from datetime import date
class aptent(BaseModel):
    client_id:int
    doc_name:str
    client_name:str
    client_mob:str
    slot:str
    da1:date