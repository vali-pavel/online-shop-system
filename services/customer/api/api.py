from sqlalchemy.orm import Session
from fastapi import Depends, Response, APIRouter

from db.db import SessionLocal
from . import schemas, db_manager
from customer import Customer

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/customers/", response_model=schemas.CustomerCreate)
def create_customer(
    new_customer: schemas.CustomerCreate, db: Session = Depends(get_db)
):
    return db_manager.create_customer(db, customer=new_customer)


@router.get("/customers/{customer_id}", response_model=schemas.CustomerBase)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db_manager.get_customer(db, customer_id)

    if not db_customer:
        return Response("Customer not found", 404)

    return db_customer


@router.get("/customers/{customer_id}/validate")
def validate_customer(customer_id, db: Session = Depends(get_db)):
    db_customer = db_manager.get_customer(db, customer_id)

    if not db_customer:
        return Response("Customer not found", 404)

    customer = Customer()
    checkout_validation = customer.validate_checkout(db_customer)

    if not checkout_validation:
        return Response(None, 422)

    return Response(None, 200)


@router.put("/customers/{customer_id}", response_model=schemas.CustomerBase)
def update_customer(
    updated_customer: schemas.CustomerBase, customer_id, db: Session = Depends(get_db)
):
    db_customer = db_manager.get_customer(db, customer_id)

    if not db_customer:
        return Response("Customer not found", 404)

    return db_manager.update_customer(db, db_customer, updated_customer)
