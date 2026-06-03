from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.deps import get_current_user
from app.crud.user import update_user
from app.schemas.user import UserRead, UserUpdate

router = APIRouter()


@router.get("/me", response_model=UserRead)
def read_current_user(current_user=Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserRead)
def update_current_user(user_update: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = update_user(db, current_user, user_update)
    return user
