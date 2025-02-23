from sqlalchemy.orm import Session
from . import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        symbol=order.symbol,
        price=order.price,
        quantity=order.quantity,
        order_type=order.order_type,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, paginate: int = 0, limit: int = 100):
    return db.query(models.Order).offset(paginate).limit(limit).all()
