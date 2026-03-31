from .schemas import apttab

def abc(dba):
    v=dba.query(apttab).all()
    return v

def sce(date,dba):
    v=dba.query(apttab).filter(apttab.date==date).all()
    if v is None:
        return{
            "status":"no apt on this date"
        }
    return v

def scb(data,dba):
    v=apttab(
             doc_name=data.doc_name,
             client_name=data.client_name,
             client_mob=data.client_mob,
             time_slot=data.slot,
             datee1=data.da1
            )
    dba.add(v)
    dba.commit()
    dba.refresh(v)
    return{
        "status": " appointment booked"
    }

def scd(i_d,dba):
    v=dba.query(apttab).filter(apttab.client_id==i_d).first()
    dba.delete(v)
    dba.commit()
    dba.refresh(v)
    if v is None:
        return {
            "status":" not any apt"
        }



