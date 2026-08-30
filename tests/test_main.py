from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Pipeline CI/CD Demo API is running"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "timestamp" in body


def test_create_item():
    payload = {"name": "example", "description": "a test item"}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json() == payload


def test_create_item_without_description():
    payload = {"name": "example"}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "example"
