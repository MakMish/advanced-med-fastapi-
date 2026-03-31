from utils.dbconnection import Base
from sqlalchemy import Column,String,Integer,CHAR,VARCHAR
class doctab(Base):
    __tablename__="doc_tab"
    doc_id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(VARCHAR(30),nullable=False)
    proffession=Column(String,nullable=False)
    password=Column(VARCHAR(10),nullable=False)
    emg_cont=Column(CHAR(10),unique=True,nullable=False)
    hospital_name=Column(String,nullable=False)
    ref_token=Column(VARCHAR(500),nullable=False)
    img_url=Column(String,default="https://png.pngtree.com/png-vector/20240122/ourmid/pngtree-doctor-symbol-color-png-image_11455717.png")
