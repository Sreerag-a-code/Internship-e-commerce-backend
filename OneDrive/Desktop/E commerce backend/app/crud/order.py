from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product


def create_order_from_cart(db: Session, cart: Cart, user_id: int) -> Order | None:
    if not cart.items:
        return None

    total = 0
    for item in cart.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product or product.stock < item.quantity:
            return None
        total += float(item.unit_price) * item.quantity

    order = Order(user_id=user_id, total=total)
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in cart.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        product.stock -= item.quantity
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
        )
        db.add(order_item)
        db.delete(item)

    db.commit()
    db.refresh(order)
    return order


def get_order(db: Session, order_id: int, user_id: int = None):
    query = db.query(Order).filter(Order.id == order_id)
    if user_id is not None:
        query = query.filter(Order.user_id == user_id)
    return query.first()


def list_user_orders(db: Session, user_id: int, skip: int = 0, limit: int = 50):
    return db.query(Order).filter(Order.user_id == user_id).offset(skip).limit(limit).all()
