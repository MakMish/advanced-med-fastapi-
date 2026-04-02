from sqlalchemy import String,Integer,Column,Boolean,VARCHAR
from SRC.utils.dbconnection import Base
class tablepro(Base):
    __tablename__="product_table"
    order_id=Column(Integer,autoincrement=True,primary_key=True)
    product=Column(String,nullable=False)
    description=Column(String,nullable=False)
    availablity=Column(Boolean,default=True)
    img_url=Column(VARCHAR(500),nullable=False)
