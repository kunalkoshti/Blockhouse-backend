from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True

class OrdersList(BaseModel):
    orders: List[Order]
