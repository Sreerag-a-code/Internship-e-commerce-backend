# E-Commerce Backend (FastAPI)
intern id- CITS2715

A production-ready portfolio backend built with FastAPI, PostgreSQL, SQLAlchemy, JWT authentication, role-based authorization, and modular clean architecture.

## Features

- FastAPI REST API
- PostgreSQL database with SQLAlchemy ORM
- Alembic migrations
- JWT-based authentication
- Admin and customer roles
- Products, categories, carts, orders, and health endpoints
- Cart operations and checkout flow
- Pagination, search, filtering, sorting
- Docker and docker-compose support
- Environment variable configuration
- Pytest test suite

## Project Structure

- `app/` – application package
  - `core/` – configuration, security, database setup
  - `models/` – SQLAlchemy models
  - `crud/` – repository operations for each domain
  - `schemas/` – Pydantic request/response models
  - `api/v1/routers/` – route modules and dependency helpers
- `alembic/` – database migration scripts
- `tests/` – integration tests with FastAPI TestClient
- `Dockerfile`, `docker-compose.yml`, `.env.example`, `requirements.txt`

## Local Setup

1. Open terminal in the project root:

```powershell
cd "c:\Users\srana\OneDrive\Desktop\E commerce backend"
```

2. Copy environment template:

```powershell
copy .env.example .env
```

3. Build containers and start services:

```powershell
docker compose up -d --build
```

4. Initialize database migrations:

```powershell
docker compose exec backend alembic upgrade head
```

5. Open API docs:

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Database Migration Commands

- Create a new revision:

```powershell
docker compose exec backend alembic revision --autogenerate -m "Add feature"
```

- Apply migrations:

```powershell
docker compose exec backend alembic upgrade head
```

- Roll back one migration:

```powershell
docker compose exec backend alembic downgrade -1
```

## Run Commands

- Start app locally without Docker:

```powershell
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

- Run tests:

```powershell
pytest -q
```

## Example API Endpoints

### Auth

- `POST /auth/register`
- `POST /auth/login`

### Users

- `GET /users/me`
- `PUT /users/me`

### Products

- `GET /products/`
- `GET /products/{product_id}`
- `POST /products/` (admin only)
- `PUT /products/{product_id}` (admin only)
- `DELETE /products/{product_id}` (admin only)

### Categories

- `GET /categories/`
- `POST /categories/` (admin only)
- `DELETE /categories/{category_id}` (admin only)

### Cart

- `GET /carts/`
- `POST /carts/items`
- `DELETE /carts/items/{item_id}`
- `DELETE /carts/`

### Orders

- `POST /orders/checkout`
- `GET /orders/`
- `GET /orders/{order_id}`

### Admin

- `GET /admin/dashboard`
- `GET /admin/users`
- `POST /admin/users/{user_id}/promote`

### Health

- `GET /health`

## Sample Request / Response

### Register

```http
POST /auth/register
Content-Type: application/json

{
  "email": "jane.doe@example.com",
  "password": "SecurePass123",
  "full_name": "Jane Doe"
}
```

```json
{
  "id": 1,
  "email": "jane.doe@example.com",
  "full_name": "Jane Doe",
  "role": "customer",
  "is_active": true
}
```

### Login

```http
POST /auth/login
Content-Type: application/json

{
  "email": "jane.doe@example.com",
  "password": "SecurePass123"
}
```

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Create Product (Admin)

```http
POST /products/
Authorization: Bearer <jwt-token>
Content-Type: application/json

{
  "title": "Bluetooth Speaker",
  "description": "Portable speaker with rich sound.",
  "price": 49.99,
  "stock": 120,
  "category_id": 1
}
```

### Checkout

```http
POST /orders/checkout
Authorization: Bearer <jwt-token>
```

```json
{
  "id": 1,
  "user_id": 2,
  "status": "pending",
  "total": 99.98,
  "items": [
    {
      "id": 1,
      "product_id": 3,
      "quantity": 2,
      "unit_price": 49.99
    }
  ],
  "created_at": "2026-06-02T00:00:00"
}
```

## GitHub Upload Steps

1. Initialize repository if needed:

```powershell
git init
git add .
git commit -m "chore: add FastAPI e-commerce backend portfolio project"
```

2. Create GitHub repository and add remote:

```powershell
git remote add origin https://github.com/<your-username>/ecommerce-backend-fastapi.git
git push -u origin main
```

3. Add a production-ready commit message and push updates regularly.

---

## Notes

- The test suite includes authentication, admin workflows, product search, cart management, and checkout.
- Use Docker Compose in local development to mirror production dependencies.
- Validate environment variables with `.env` and `.env.example`.
