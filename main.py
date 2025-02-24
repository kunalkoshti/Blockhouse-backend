from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import get_db, Base, engine
from . import crud, models, schemas, db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"API working!!"}

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(db.get_db)):
    try:
        return crud.create_order(db=db, order=order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/orders/", response_model=schemas.OrdersList)
def get_orders(paginate: int = 0, limit: int = 100, db: Session = Depends(db.get_db)):
    orders = crud.get_orders(db=db, paginate=paginate, limit=limit)
    return {"orders": orders }