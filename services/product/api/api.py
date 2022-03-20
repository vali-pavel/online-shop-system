from sqlalchemy.orm import Session
from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
    status,
    UploadFile,
    File,
    Form,
)
from fastapi_pagination import Page, paginate, Params
from typing import List, Optional
import base64

from db.db import SessionLocal
from . import schemas, db_manager
from product import Product
import constants

router = APIRouter(prefix="/api")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/products", response_model=schemas.CreatedProduct)
def create_product(new_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    try:
        db_product = db_manager.create_product(db, new_product)
        return db_product
    except:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY)


@router.post("/products/upload")
async def upload_image(
    product_id: int = Form(...),
    files: List[UploadFile] = File(...),
):
    product = Product()
    for file in files:
        content = await file.read()
        is_image_file = product.validate_file_type(content)
        if is_image_file:
            product.resize_and_save_img(content, file.filename, product_id)


@router.get("/products/{product_id}", response_model=schemas.ProductBase)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_response = db_manager.get_product(db, product_id)
    if not db_response:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Product not found")
    return db_response


@router.get("/products", response_model=Page[schemas.ProductBase])
def get_products(
    page_number: Optional[str] = 0,
    user_id: Optional[int] = None,
    category: Optional[int] = None,
    db: Session = Depends(get_db),
):
    filters = schemas.ProductFilters(user_id=user_id, category=category)
    query_filters = db_manager.filter_products(db, filters)
    db_products = db_manager.get_products(query_filters)

    return paginate(db_products, Params(page=page_number, size=constants.PAGE_SIZE))


@router.get("/products/{product_id}/images")
def get_product_images(product_id: int):
    product = Product()
    images = product.get_images(product_id)

    base64images = []
    for image in images:
        with open(image.file_path, "rb") as f:
            base64images.append(base64.b64encode(f.read()))

    return base64images


@router.get("/products/{product_id}/inventory", response_model=schemas.ProductInventory)
def get_product_inventory(product_id: int, db: Session = Depends(get_db)):
    db_response = db_manager.get_product(db, product_id)
    if not db_response:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Product not found")
    return db_response


@router.put("/products/{product_id}/inventory")
def update_product_inventory(
    product_id: int,
    inventory: schemas.ProductInventory,
    db: Session = Depends(get_db),
):
    db_product = db_manager.get_product(db, product_id)
    if not db_product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Product not found")

    return db_manager.update_product_inventory(db, db_product, inventory.inventory)
