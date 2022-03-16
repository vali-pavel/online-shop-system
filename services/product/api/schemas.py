from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    sku: str = Field(...)
    price: float = Field(...)
    color: str = Field(...)
    inventory: int = Field(...)
    min_delivery_days: int = Field(...)
    max_delivery_days: int = Field(...)
    vendor_name: str = Field(...)
    category: int = Field(...)

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    user_id: int = Field(...)


class ProductFilters(BaseModel):
    user_id: Optional[int]
    category: Optional[int]
