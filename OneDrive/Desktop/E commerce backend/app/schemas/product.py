from typing import Optional
from pydantic import BaseModel, condecimal

from app.schemas.category import CategoryRead


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: condecimal(gt=0, max_digits=12, decimal_places=2)
    stock: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[condecimal(gt=0, max_digits=12, decimal_places=2)]
    stock: Optional[int]
    category_id: Optional[int]


class ProductRead(ProductBase):
    id: int
    category: Optional[CategoryRead]

    class Config:
        orm_mode = True
