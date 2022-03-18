from sqlalchemy.orm import Session
from fastapi import Depends, Response, APIRouter, HTTPException, status

from db.db import SessionLocal
from . import schemas, db_manager
from customer import Customer

router = APIRouter(prefix="/api")


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


@router.get("/customers/{user_id}", response_model=schemas.CustomerBase)
def read_customer(user_id: int, db: Session = Depends(get_db)):
    db_customer = db_manager.get_customer(db, user_id)

    if not db_customer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Customer not found")

    return db_customer


@router.get("/customers/{user_id}/validate")
def validate_customer(user_id: int, db: Session = Depends(get_db)):
    db_customer = db_manager.get_customer(db, user_id)

    if not db_customer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Customer not found")

    customer = Customer()
    checkout_validation = customer.validate_checkout(db_customer)

    if not checkout_validation:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, "Invalid customer fields"
        )

    return Response(None, 200)


@router.put("/customers/{user_id}", response_model=schemas.CustomerBase)
def update_customer(
    updated_customer: schemas.CustomerBase, user_id: int, db: Session = Depends(get_db)
):
    db_customer = db_manager.get_customer(db, user_id)

    if not db_customer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Customer not found")

    return db_manager.update_customer(db, db_customer, updated_customer)
