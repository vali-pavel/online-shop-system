from pydantic import BaseModel, Field


class Order(BaseModel):
    product_id: int = Field(...)
    user_id: int = Field(...)
    quantity: int = Field(...)
