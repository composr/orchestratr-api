import unittest
from unittest.mock import Mock, patch
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..\\..")
sys.path.append(topdir)
from app.workflow.wf_router import prefect_run_flow
import asyncio
loop = asyncio.get_event_loop()


class test_prefect_flow(unittest.TestCase):
    @patch('app.workflow.wf_router.prefect_flow')
    def test_prefect(self, response_mock):
        response_mock.return_value = 'flow_run_id_value'
        print(response_mock.return_value)

        print(loop.run_until_complete(prefect_run_flow("test_project", "test_flow")))
        assert loop.run_until_complete(prefect_run_flow("test_project", "test_flow")) == {'flow_run_id': 'flow_run_id_value'}


if __name__ == '__main__':
    unittest.main()