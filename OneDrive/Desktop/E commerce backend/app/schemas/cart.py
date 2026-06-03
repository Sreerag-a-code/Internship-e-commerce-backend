from typing import List
from pydantic import BaseModel, PositiveInt


class CartItemBase(BaseModel):
    product_id: int
    quantity: PositiveInt


class CartItemCreate(CartItemBase):
    pass


class CartItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        orm_mode = True


class CartRead(BaseModel):
    id: int
    items: List[CartItemRead]
    created_at: str

    class Config:
        orm_mode = True
