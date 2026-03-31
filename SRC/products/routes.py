from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from utils.dbconnection import get_db
from .models import tabent1
import services
router=APIRouter(prefix="/products")

@router.get("/all")
def hex(dba:Session=Depends(get_db)):
        return services.xsz(dba)    
@router.post("/give",status_code=201)
def  vex(data:tabent1,dba:Session=Depends(get_db)):
        return services.cse(data,dba)

@router.delete("/cancel")
def rex(i_d:int,dba:Session=Depends(get_db)):
        return services.cce(i_d,dba)

