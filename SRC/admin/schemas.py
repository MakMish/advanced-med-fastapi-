from datetime import datetime
import pytz
from sqlalchemy import Integer,DateTime,Column,Boolean
from utils.dbconnection import Base
class tablerec(Base):
    __tablename__="admin_table"
    total_orders=Column(Integer)
    total_amt=Column(Integer)
    date=Column(DateTime,default=datetime.now(pytz.timezone("Asia/Kolkata")).date(),primary_key=True)
