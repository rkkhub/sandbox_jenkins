import pytest

from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is named 'app'

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'FastApi hellow w'}