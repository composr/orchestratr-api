import unittest
import pytest
from pytest_mock import mocker
from unittest.mock import Mock, patch
from fastapi.testclient import TestClient
import os, sys
topdir = os.path.join(os.path.dirname(__file__), "..\\..")
sys.path.append(topdir)
from app.main import app
from app.workflow.wf_service import prefect_flow, client

test_client = TestClient(app)

class test_prefect_flow(unittest.TestCase):
    #@patch.object(client, "graphql", side_effect=["test1s", "test2s"])
    @patch("app.workflow.wf_service.client.graphql", return_value={"data":{"flow":[{"id":1}]}})
    @patch("app.workflow.wf_service.client.create_flow_run", return_value="test_id")
    def test_prefect_flow(self, s1, s2):
        #m = mocker.patch("app.workflow.wf_service.client.graphql", return_value="test")

        response = test_client.post("/workflow/test_project/test_flow")
        print(response)
        print("*********------*********")
        #print(s1.call_args_list)
        #print(s1.call_count)
        assert prefect_flow("test_project", "test_flow") == "test_id"
        #s1.assert_called_with(project_id_by_name, variables={'project_name': "test_project"})
        print(s2.call_args_list)
        print(s2.call_count)

if __name__ == '__main__':
    unittest.main()