from typing import List
from pydantic import BaseModel, PositiveInt, condecimal


class OrderItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        orm_mode = True


class OrderRead(BaseModel):
    id: int
    user_id: int
    status: str
    total: condecimal(gt=0, max_digits=14, decimal_places=2)
    items: List[OrderItemRead]
    created_at: str

    class Config:
        orm_mode = True
