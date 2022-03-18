from datetime import date
from pydantic import BaseModel, Field
from typing import Optional


class CustomerBase(BaseModel):
    id: Optional[int]
    shipping_address: Optional[str]
    billing_address: Optional[str]
    card_number: Optional[int]
    card_expiration: Optional[date]
    card_holder: Optional[str]

    class Config:
        orm_mode = True


class CustomerCreate(CustomerBase):
    user_id: int = Field(...)

    class Config:
        orm_mode = True
