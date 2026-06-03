from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def list_products(db: Session, skip: int = 0, limit: int = 50, search: str | None = None, sort: str = "id"):
    base = db.query(Product)
    if search:
        base = base.filter(or_(Product.title.ilike(f"%{search}%"), Product.description.ilike(f"%{search}%")))
    if sort.startswith("-"):
        base = base.order_by(getattr(Product, sort[1:]).desc())
    else:
        base = base.order_by(getattr(Product, sort).asc())
    return base.offset(skip).limit(limit).all()


def create_product(db: Session, product_in: ProductCreate):
    product = Product(**product_in.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product: Product, product_in: ProductUpdate):
    for field, value in product_in.dict(exclude_unset=True).items():
        setattr(product, field, value)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product):
    db.delete(product)
    db.commit()
    return product
