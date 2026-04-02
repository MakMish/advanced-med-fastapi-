from SRC.utils.dbconnection import Base
from datetime import datetime
import pytz
from sqlalchemy import Column,String,Integer,CHAR,VARCHAR,Date
def get_ist_time():
    return datetime.now(pytz.timezone("Asia/Kolkata")).date()
class apttab(Base):
    __tablename__="apt_tab"
    client_id=Column(Integer,autoincrement=True,primary_key=True)
    doc_name=Column(String,nullable=False)
    client_name=Column(String,nullable=False)
    client_mob=Column(CHAR(100),nullable=False)
    time_slot=Column(VARCHAR(10),nullable=False)
    datee1=Column(Date,default=get_ist_time,nullable=False)
