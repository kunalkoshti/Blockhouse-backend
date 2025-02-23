from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import get_db, Base, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"API working!!"}

