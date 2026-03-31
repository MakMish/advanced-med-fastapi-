from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from utils.dbconnection import get_db
from .schemas import tablerec
from .models import xer

def abc(dba):
    p=dba.query(tablerec).all()
    return{
        "data":p
    }

def dce(m,dba):
    v=dba.query(tablerec).filter(tablerec.date==m).all()
    if v is None:
        return{
            "status":"invalid date"
        }
    return v