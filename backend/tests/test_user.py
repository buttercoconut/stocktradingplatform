# tests/test_user.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_user():
    def _create_user(username, email, password):
        return client.post("/users/", json={"username": username, "email": email, "password": password})
    return _create_user


def test_create_user(create_user):
    response = create_user("alice", "alice@example.com", "secret123")
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"


def test_duplicate_user(create_user):
    create_user("bob", "bob@example.com", "secret123")
    response = create_user("bob", "bob2@example.com", "secret123")
    assert response.status_code == 400
