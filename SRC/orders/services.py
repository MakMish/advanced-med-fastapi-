from .schemas import table1  

def xsz(dba):
    v=dba.query(table1).all()
    dba.commit()
    return{
        "orders":v
    }


def  cse(data, dba):
            m=table1(
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
       x=dba.query(table1).filter(table1.order_id==i_d).first()
       dba.delete(x)
       dba.commit()
       dba.refresh(x)
       return{
        "status":" order cancelled"
       }