from datetime import datetime
import pytz
from sqlalchemy import String,Integer,DateTime,Column,Boolean
from utils.dbconnection import Base
class table1(Base):
    __tablename__="order_table"
    order_id=Column(Integer,autoincrement=True,primary_key=True)
    product=Column(String,nullable=False)
    quantity=Column(Integer,nullable=False)
    order_status=Column(Boolean,default=False)
    time=Column(DateTime,default=datetime.now(pytz.timezone("Asia/Kolkata")))
  