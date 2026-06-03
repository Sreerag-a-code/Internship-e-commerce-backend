from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.deps import get_current_user
from app.crud.cart import add_item_to_cart, clear_cart, get_or_create_cart, remove_item_from_cart
from app.schemas.cart import CartItemCreate, CartRead

router = APIRouter()


@router.get("/", response_model=CartRead)
def read_cart(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    cart = get_or_create_cart(db, current_user.id)
    return cart


@router.post("/items", response_model=CartRead, status_code=status.HTTP_201_CREATED)
def add_cart_item(item_in: CartItemCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    cart = get_or_create_cart(db, current_user.id)
    item = add_item_to_cart(db, cart, item_in)
    if not item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product unavailable or stock insufficient")
    db.refresh(cart)
    return cart


@router.delete("/items/{item_id}", response_model=CartRead)
def delete_cart_item(item_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    cart = get_or_create_cart(db, current_user.id)
    removed = remove_item_from_cart(db, cart, item_id)
    if not removed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")
    db.refresh(cart)
    return cart


@router.delete("/", response_model=CartRead)
def clear_cart_endpoint(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    cart = get_or_create_cart(db, current_user.id)
    clear_cart(db, cart)
    db.refresh(cart)
    return cart
