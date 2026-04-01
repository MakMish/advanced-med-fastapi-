from fastapi import FastAPI,Depends
from google import genai
from admin.routes import routes2 as rec_router
from pydantic import BaseModel
from model import setting
from orders.routes import router as order_router
from users.routes import router as user_router
from utils.dbconnection import get_db
from sqlalchemy.orm import Session
from doctors.routes import router as doc_route
from appointment.routes import router as apt_route
from datetime import datetime
import pytz
from products.routes import router as product_router
from utils.dbconnection import Base,engine
from fastapi.middleware.cors import CORSMiddleware
async def init_db():
      async with engine.begin() as conn:
            await conn.run_sync(Base.metadata)
mas=setting()
class data(BaseModel):
    rext:str
app=FastAPI()
app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_headers=["*"],
      allow_methods=["*"]
)

app.include_router(order_router)
app.include_router(rec_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(doc_route)
app.include_router(apt_route)
@app.post("/ai")
async def gt(tes:data,dba:Session=Depends(get_db)):
        Limit=5
        x=datetime.now(pytz.timezone("Asia/kolkata")).date()
        client=genai.Client(api_key=setting().gapi_key)
        response=client.models.generate_content(
              model="gemini-2.5-flash-lite",
              contents=f"""
                    You are a helpful assistant.
                    For common minor health issues, you can suggest general over-the-counter medicines with price range.
                    Always include a disclaimer to consult a doctor.

                        Question: {tes.rext}
                        """
        )    
        return{
              "status":str(response.text)
        }
@app.get("/test")
def casr():
      print(" working_________")
      return{
            "status":"good"
      }

