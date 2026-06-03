from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def list_categories(db: Session, skip: int = 0, limit: int = 50):
    return db.query(Category).offset(skip).limit(limit).all()


def create_category(db: Session, category_in: CategoryCreate):
    category = Category(**category_in.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category: Category):
    db.delete(category)
    db.commit()
    return category
