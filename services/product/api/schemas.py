from pydantic import BaseModel, Field
from typing import Optional


class ProductInventory(BaseModel):
    inventory: int = Field(...)

    class Config:
        orm_mode = True


class ProductBase(ProductInventory):
    id: Optional[int] = Field(...)
    sku: str = Field(...)
    name: str = Field(...)
    price: float = Field(...)
    color: str = Field(...)
    min_delivery_days: int = Field(...)
    max_delivery_days: int = Field(...)
    vendor_name: str = Field(...)
    category: int = Field(...)


class ProductCreate(ProductBase):
    user_id: int = Field(...)


class CreatedProduct(BaseModel):
    id: int = Field(...)

    class Config:
        orm_mode = True


class ProductFilters(BaseModel):
    user_id: Optional[int]
    category: Optional[int]
