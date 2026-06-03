from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user_in: UserCreate, role: str = "customer") -> User:
    user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
        role=role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User, user_in: UserUpdate):
    if user_in.full_name is not None:
        user.full_name = user_in.full_name
    if user_in.password:
        user.hashed_password = get_password_hash(user_in.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session, skip: int = 0, limit: int = 50):
    return db.query(User).offset(skip).limit(limit).all()
