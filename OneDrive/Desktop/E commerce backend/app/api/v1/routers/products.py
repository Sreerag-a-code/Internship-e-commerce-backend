from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud.product import create_product, delete_product, get_product, list_products, update_product
from app.api.deps import require_admin
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate

router = APIRouter()


@router.get("/", response_model=List[ProductRead])
def read_products(
    skip: int = 0,
    limit: int = Query(20, le=100),
    search: str | None = None,
    sort: str = "id",
    db: Session = Depends(get_db),
):
    return list_products(db, skip=skip, limit=limit, search=search, sort=sort)


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(product_in: ProductCreate, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    return create_product(db, product_in)


@router.get("/{product_id}", response_model=ProductRead)
def get_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductRead)
def update_product_endpoint(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return update_product(db, product, product_in)


@router.delete("/{product_id}", response_model=ProductRead)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return delete_product(db, product)
