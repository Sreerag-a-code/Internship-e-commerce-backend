import os

os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")
os.environ.setdefault("APP_SECRET_KEY", "testsecretkey123")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "60")

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import get_db
from app.crud.user import create_user, get_user_by_email
from app.main import app
from app.models.base import Base
from app.schemas.user import UserCreate

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, future=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base.metadata.create_all(bind=engine)

with TestingSessionLocal() as session:
    if not get_user_by_email(session, "admin@example.com"):
        admin_in = UserCreate(email="admin@example.com", password="AdminPass123", full_name="Admin")
        create_user(session, admin_in, role="admin")


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
