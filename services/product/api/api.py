from dataclasses import dataclass
from unicodedata import category
from sqlalchemy.orm import Session
from fastapi import Depends, Response, APIRouter, HTTPException, status
from fastapi_pagination import Page, add_pagination, paginate, Params
from typing import Optional

from db.db import SessionLocal
from db import models

from . import schemas, db_manager


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/products", response_model=schemas.ProductCreate)
def create_product(new_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    try:
        db_product = db_manager.create_product(db, new_product)
        return db_product
    except:
        return HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.post("/products/upload")
def upload_image():
    pass


@router.get("/products/{product_id}", response_model=schemas.ProductBase)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_response = db_manager.get_product(db, product_id)
    if not db_response:
        return HTTPException(status.HTTP_404_NOT_FOUND, "Product not found")
    return db_response


@router.get("/products", response_model=Page[schemas.ProductBase])
def get_products(
    page_number: Optional[int],
    size: Optional[int],
    filters: schemas.ProductFilters,
    db: Session = Depends(get_db),
):
    query_filters = db_manager.filter_products(db, filters)
    db_products = db_manager.get_products(query_filters)

    return paginate(db_products, Params(page=page_number, size=size))
