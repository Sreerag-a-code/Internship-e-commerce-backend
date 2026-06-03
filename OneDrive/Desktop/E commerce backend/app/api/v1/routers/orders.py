from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.deps import get_current_user
from app.crud.cart import get_or_create_cart
from app.crud.order import create_order_from_cart, get_order, list_user_orders
from app.schemas.order import OrderRead

router = APIRouter()


@router.post("/checkout", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def checkout(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    cart = get_or_create_cart(db, current_user.id)
    order = create_order_from_cart(db, cart, current_user.id)
    if not order:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Checkout failed due to invalid cart or stock")
    return order


@router.get("/", response_model=List[OrderRead])
def read_orders(skip: int = 0, limit: int = 50, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return list_user_orders(db, current_user.id, skip=skip, limit=limit)


@router.get("/{order_id}", response_model=OrderRead)
def read_order(order_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    order = get_order(db, order_id, current_user.id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order
