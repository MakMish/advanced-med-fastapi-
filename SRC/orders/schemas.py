from datetime import datetime
from sqlalchemy import String,Integer,DateTime,Column,Boolean,VARCHAR
from SRC.utils.dbconnection import Base
def time():
     tym=datetime.now().date()
     return tym
class table1(Base):
    __tablename__="order_table"
    order_id=Column(Integer,autoincrement=True,primary_key=True)
    product=Column(String,nullable=False)
    quantity=Column(Integer,nullable=False)
    order_status=Column(Boolean,default=False)
    uaddress=Column(VARCHAR(30),nullable=False)
    time=Column(DateTime,default=time)
  