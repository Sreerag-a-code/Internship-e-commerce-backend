from tests.conftest import client


def test_admin_create_and_search_product():
    login = client.post("/auth/login", json={"email": "admin@example.com", "password": "AdminPass123"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    category = client.post("/categories/", json={"name": "Electronics"}, headers=headers)
    assert category.status_code == 201
    category_id = category.json()["id"]

    product = client.post(
        "/products/",
        json={"title": "Wireless Mouse", "description": "Comfortable wireless mouse.", "price": 29.99, "stock": 150, "category_id": category_id},
        headers=headers,
    )
    assert product.status_code == 201
    assert product.json()["title"] == "Wireless Mouse"

    search = client.get("/products/?search=wireless&sort=-price")
    assert search.status_code == 200
    assert any(item["title"] == "Wireless Mouse" for item in search.json())
