from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from utils.dbconnection import get_db
from .schemas import table1  
import services
from .models import tabent
router=APIRouter(prefix="/orders")

@router.get("/all")
def hex(dba:Session=Depends(get_db)):
       return services.xsz(dba)
    
@router.post("/give",status_code=201)
def vex(data:tabent, dba:Session=Depends(get_db)):
      return services.cse(data,dba)

@router.delete("/cancel")
def rex(i_d:int,dba:Session=Depends(get_db)):
        return services.cce(i_d,dba)
          
