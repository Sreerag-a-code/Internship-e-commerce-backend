from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product
from app.schemas.cart import CartItemCreate


def get_or_create_cart(db: Session, user_id: int) -> Cart:
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    if cart is None:
        cart = Cart(user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart


def add_item_to_cart(db: Session, cart: Cart, item_in: CartItemCreate):
    product = db.query(Product).filter(Product.id == item_in.product_id).first()
    if not product or product.stock < item_in.quantity:
        return None
    existing = (
        db.query(CartItem)
        .filter(CartItem.cart_id == cart.id)
        .filter(CartItem.product_id == item_in.product_id)
        .first()
    )
    if existing:
        existing.quantity += item_in.quantity
        existing.unit_price = product.price
        db.add(existing)
        db.commit()
        db.refresh(existing)
        return existing

    cart_item = CartItem(
        cart_id=cart.id,
        product_id=item_in.product_id,
        quantity=item_in.quantity,
        unit_price=product.price,
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item


def remove_item_from_cart(db: Session, cart: Cart, item_id: int):
    item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.cart_id == cart.id).first()
    if item:
        db.delete(item)
        db.commit()
    return item


def clear_cart(db: Session, cart: Cart):
    for item in cart.items:
        db.delete(item)
    db.commit()
    return cart
