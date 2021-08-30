from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from app.main import app

"""
TODO: 
Refactor based on docs 
"""

client = TestClient(app)


def test_liveness():
    response = client.get("/liveness")
    assert response.status_code == 200
    assert response.json() == {"Message": "i am alive"}
