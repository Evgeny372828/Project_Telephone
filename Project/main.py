from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
app = FastAPI()


@app.get("/")
def read_root():
    html_content = "Hello "
    return html_content
