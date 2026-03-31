from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from model import setting
mas=setting()
engine=create_engine(mas.url)
Base=declarative_base()
localsession=sessionmaker(bind=engine)
def get_db():
    db=localsession()
    try:
        yield db
    finally:
        db.close()

