from fastapi import FastAPI

from app.api.v1.routers.admin import router as admin_router
from app.api.v1.routers.auth import router as auth_router
from app.api.v1.routers.categories import router as categories_router
from app.api.v1.routers.carts import router as carts_router
from app.api.v1.routers.health import router as health_router
from app.api.v1.routers.orders import router as orders_router
from app.api.v1.routers.products import router as products_router
from app.api.v1.routers.users import router as users_router


def register_routes(app: FastAPI) -> None:
    app.include_router(health_router)
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(users_router, prefix="/users", tags=["users"])
    app.include_router(categories_router, prefix="/categories", tags=["categories"])
    app.include_router(products_router, prefix="/products", tags=["products"])
    app.include_router(carts_router, prefix="/carts", tags=["carts"])
    app.include_router(orders_router, prefix="/orders", tags=["orders"])
    app.include_router(admin_router, prefix="/admin", tags=["admin"])
