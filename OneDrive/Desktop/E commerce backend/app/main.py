from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.routers import register_routes
from app.core.database import engine
from app.models.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routes(app)
