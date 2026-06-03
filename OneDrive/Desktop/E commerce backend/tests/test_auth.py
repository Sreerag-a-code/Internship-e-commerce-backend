from tests.conftest import client


def test_register_and_login():
    payload = {"email": "customer@example.com", "password": "StrongPass123", "full_name": "Customer"}
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]

    login_response = client.post("/auth/login", json={"email": payload["email"], "password": payload["password"]})
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()


def test_register_duplicate_email():
    payload = {"email": "duplicate@example.com", "password": "StrongPass123", "full_name": "Duplicate"}
    client.post("/auth/register", json=payload)
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 409
    assert response.json()["detail"] == "Email already registered"
