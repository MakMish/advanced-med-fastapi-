from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from utils.dbconnection import get_db
from .schemas import tablerec
from .models import xer
import services

routes2=APIRouter(
    prefix="/history"
)


@routes2.get("/order_all")
def hex(dba:Session=Depends(get_db)):
    return services.abc(dba)
    


@routes2.get("/order")
def rex(m:xer,dba:Session=Depends(get_db)):
    return services.dce(m,dba)
    