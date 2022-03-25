from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.workflow.wf_service import prefect_flow

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

@patch("app.workflow.wf_service.client.graphql", side_effects=[{"data":{"project":[{"id":1}]}}, {"data":{"flow":[{"id":1}]}}])
@patch("app.workflow.wf_service.client.create_flow_run", return_value="test_id")
def test_prefect_flow(s1, s2):
    response = client.post("/workflow/test_project/test_flow")
    assert prefect_flow("test_project", "test_flow") == "test_id"
