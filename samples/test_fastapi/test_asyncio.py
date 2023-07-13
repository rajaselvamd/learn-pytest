from typing import AsyncIterator
import httpx
import pytest
import pytest_asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Hello World"}

@pytest_asyncio.fixture()
async def client() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest.mark.asyncio
async def test_home(client: httpx.AsyncClient) -> None:
    response = await client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}