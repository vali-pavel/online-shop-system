from sqlalchemy.orm import Session, Query

from . import schemas
from db import models


def get_product(db: Session, product_id: int) -> schemas.ProductBase:
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(
    db: Session, new_product: schemas.ProductCreate
) -> schemas.CreatedProduct:
    db_product = models.Product(
        name=new_product.name,
        user_id=new_product.user_id,
        sku=new_product.sku,
        price=new_product.price,
        color=new_product.color,
        inventory=new_product.inventory,
        min_delivery_days=new_product.min_delivery_days,
        max_delivery_days=new_product.max_delivery_days,
        vendor_name=new_product.vendor_name,
        category=new_product.category,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(query_filters: Query):
    return query_filters.all()


def filter_products(db: Session, filters: schemas.ProductFilters):
    query_filters = None
    if filters.category != None:
        query_filters = db.query(models.Product).filter(
            models.Product.category == filters.category
        )
    if filters.user_id != None:
        query_filters = db.query(models.Product).filter(
            models.Product.user_id == filters.user_id
        )
    if query_filters == None:
        query_filters = db.query(models.Product)
    return query_filters


def update_product_inventory(
    db: Session, existing_inventory: schemas.ProductInventory, new_inventory: int
):
    existing_inventory.inventory = new_inventory
    db.commit()
    db.refresh(existing_inventory)
    return existing_inventory
