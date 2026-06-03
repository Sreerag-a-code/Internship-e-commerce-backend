from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud.category import create_category, delete_category, get_category, list_categories
from app.api.deps import require_admin
from app.schemas.category import CategoryCreate, CategoryRead

router = APIRouter()


@router.get("/", response_model=List[CategoryRead])
def read_categories(skip: int = 0, limit: int = Query(50, le=100), db: Session = Depends(get_db)):
    return list_categories(db, skip=skip, limit=limit)


@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category_endpoint(category_in: CategoryCreate, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    return create_category(db, category_in)


@router.delete("/{category_id}", response_model=CategoryRead)
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    category = get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return delete_category(db, category)
