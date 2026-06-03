from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import require_admin
from app.core.database import get_db
from app.crud.category import list_categories
from app.crud.product import list_products
from app.crud.user import get_user, list_users
from app.schemas.category import CategoryRead
from app.schemas.product import ProductRead
from app.schemas.user import UserRead

router = APIRouter()


@router.get("/dashboard")
def admin_dashboard(db: Session = Depends(get_db), _: str = Depends(require_admin)):
    categories = list_categories(db, skip=0, limit=20)
    products = list_products(db, skip=0, limit=20)
    return {
        "categories_count": len(categories),
        "products_count": len(products),
        "active_categories": [CategoryRead.from_orm(category) for category in categories],
        "recent_products": [ProductRead.from_orm(product) for product in products],
    }


@router.get("/users", response_model=List[UserRead])
def admin_list_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    return list_users(db, skip=skip, limit=limit)


@router.post("/users/{user_id}/promote", response_model=UserRead)
def promote_user(user_id: int, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.role = "admin"
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
