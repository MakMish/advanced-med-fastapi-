from .schemas import tablepro
def xsz(db):
    v=db.query(tablepro).all()
    if v is None:
            return{
                    "status":"no order"
            }
    db.commit()
    return{
        "products":v
    }
    
def  cse(data,dba):
            m=tablepro(
            product=data.product,
            quantity=data.quantity
                 )
            dba.add(m)
            dba.commit()
            dba.refresh(m)
            return{
                "status":"data added"
            }
def cce(i_d,dba):
       x=dba.query(tablepro).filter(tablepro.order_id==i_d).first()
       dba.delete(x)
       dba.commit()
       dba.refresh(x)
       return{
        "status":" product cancelled"
       }


