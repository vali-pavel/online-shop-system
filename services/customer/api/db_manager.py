from sqlalchemy.orm import Session

from . import schemas
from db import models


def get_customer(db: Session, user_id: int):
    return db.query(models.Customer).filter(models.Customer.user_id == user_id).first()


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(
        user_id=customer.user_id,
        shipping_address=customer.shipping_address,
        billing_address=customer.billing_address,
        card_number=customer.card_number,
        card_expiration=customer.card_expiration,
        card_holder=customer.card_holder,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def update_customer(
    db: Session,
    existing_customer: schemas.CustomerBase,
    updated_customer: schemas.CustomerBase,
):
    existing_customer.shipping_address = updated_customer.shipping_address
    existing_customer.billing_address = updated_customer.billing_address
    existing_customer.card_number = updated_customer.card_number
    existing_customer.card_expiration = updated_customer.card_expiration
    existing_customer.card_holder = updated_customer.card_holder
    db.commit()
    db.refresh(existing_customer)
    return existing_customer
