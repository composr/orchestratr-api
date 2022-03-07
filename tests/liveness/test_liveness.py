from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_liveness():
    response = client.get("/liveness")
    assert response.status_code == 200
    assert response.json() == {"Message": "i am alive"}
