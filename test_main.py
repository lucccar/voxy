from fastapi import FastAPI
from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

test_map = {"word": "hello, world, world", "delimiters": [","]}


def test_read_main():
    response = client.post("/count", headers={"X-Token": "hailhydra"}, json=test_map)
    assert response.status_code == 200
    assert response.json() == 2
