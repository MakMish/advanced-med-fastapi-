from utils.dbconnection import Base
from datetime import datetime
import pytz

from sqlalchemy import Column,String,Integer,CHAR,Sequence,Date
def get_ist_time():
    return datetime.now(pytz.timezone("Asia/Kolkata")).date()
class user_table(Base):
    __tablename__="user_table"
    id=Column(Integer,Sequence('user_id_seq', start=260315),primary_key=True)
    uname=Column(String(20),nullable=False)
    uemail=Column(String(40),nullable=False,unique=True)
    hash_upassword=Column(String(500),nullable=False)
    umobile=Column(CHAR(10),nullable=False,unique=True)
    uaddress=Column(String(50),nullable=False)
    ref_token=Column(String(500),nullable=False)
    current_date=Column(Date,default=get_ist_time)    