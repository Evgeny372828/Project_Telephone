from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
app = FastAPI()

class Company(Base):
    __tablename__="company"

    id=Column(Integer,primary_key=True,index=True)
    name_company=Column(String,unique=True, index=True)




@app.get("/")
def read_root():
    html_content = "Hello "
    return html_content
