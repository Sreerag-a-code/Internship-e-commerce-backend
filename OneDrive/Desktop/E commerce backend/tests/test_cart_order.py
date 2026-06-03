from tests.conftest import client


def test_cart_and_checkout_flow():
    payload = {"email": "shopper@example.com", "password": "Shopper123", "full_name": "Shopper"}
    client.post("/auth/register", json=payload)
    login = client.post("/auth/login", json={"email": payload["email"], "password": payload["password"]})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    admin_login = client.post("/auth/login", json={"email": "admin@example.com", "password": "AdminPass123"})
    admin_token = admin_login.json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    category = client.post("/categories/", json={"name": "Home"}, headers=admin_headers)
    category_id = category.json()["id"]

    product = client.post(
        "/products/",
        json={"title": "Coffee Mug", "description": "Ceramic mug.", "price": 12.5, "stock": 25, "category_id": category_id},
        headers=admin_headers,
    )
    product_id = product.json()["id"]

    add_response = client.post("/carts/items", json={"product_id": product_id, "quantity": 2}, headers=headers)
    assert add_response.status_code == 201
    assert add_response.json()["items"][0]["quantity"] == 2

    checkout = client.post("/orders/checkout", headers=headers)
    assert checkout.status_code == 201
    assert checkout.json()["status"] == "pending"
