import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.on_event("startup")
def startup():
    raise Exception("Something went wrong")

@app.get("/api/endpoint")
def my_api_endpoint():
    return {"message": "Hello, World!"}

# using pytest fixture
'''
@pytest.fixture
def client():
    return TestClient(app)                  # this will not call startup!
'''
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client                        # this will call startup as part of app event

def test_api_endpoint_02(client):
    response = client.get("/api/endpoint")  # simulate a GET request to /api/endpoint
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


