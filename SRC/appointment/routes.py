from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from datetime import date
import services
from utils.dbconnection import get_db
from .models import aptent


router=APIRouter(prefix="/apt")

@router.get("/all")
def hex(dba:Session=Depends(get_db)):
    return services.abc(dba)



@router.get("/bydate")          #24-05-2946
def vex(date:date,dba:Session=Depends(get_db)):
    return services.sce(date,dba)
    
@router.post("/book")          #24-05-2946
def rex(data:aptent,dba:Session=Depends(get_db)):
    return services.scb(data,dba)


@router.delete("/cancel/{i_d}")          #24-05-2946
def dex(i_d:int,dba:Session=Depends(get_db)):
    return services.scd(i_d,dba)
   
    