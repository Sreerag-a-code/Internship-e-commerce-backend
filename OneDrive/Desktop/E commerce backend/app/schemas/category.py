from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int

    class Config:
        orm_mode = True
