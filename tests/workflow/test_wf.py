from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_status():
    response = client.get("/workflow")
    assert response.status_code == 200
    assert response.json() == {"workflow": "can't start because there aren't any!"}


def test_start_wf():
    response = client.post("/workflow", json={"namespace": "foo", "correlation_id": "bar"})
    assert response.status_code == 200
    assert response.json() == {"namespace": "foo", "correlation_id": "bar", "status": "In Progress"}

def test_start_wf_no_body():
    response = client.post("/workflow")
    assert response.status_code == 422

def test_prefect_flow():
    response = client.post("/workflow/test_project/test_flow")
    assert response.status_code == 200
    assert response.json == {"flow_run_id": "flow_run_id_value"}
