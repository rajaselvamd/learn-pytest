import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from hello import Hello  # assuming 'app' is your FastAPI application instance

app = FastAPI()

@app.get("/api/endpoint")
def my_api_endpoint():
    return {"message": "Hello, World!"}

client1 = TestClient(app)

def test_api_endpoint_01():
    response = client1.get("/api/endpoint")  # simulate a GET request to /api/endpoint
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

# using pytest fixture

@pytest.fixture
def client():
    return TestClient(app)

def test_api_endpoint_02(client):
    response = client.get("/api/endpoint")  # simulate a GET request to /api/endpoint
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


