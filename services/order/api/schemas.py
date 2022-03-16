from pydantic import BaseModel, Field


class Order(BaseModel):
    product_id: int = Field(...)
    customer_id: int = Field(...)
    quantity: int = Field(...)
