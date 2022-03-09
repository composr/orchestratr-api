from fastapi import APIRouter, Request, Response, Body, HTTPException, Header
from fastapi.responses import PlainTextResponse

from .wf_models import StartWorkflowRequest, WorkflowResponse
from app.topology.topology_models import Topology

router = APIRouter()

@router.get("", status_code=200)
async def wf_status():
    return {"workflow": "can't start because there aren't any!"}

@router.post("", response_model=WorkflowResponse)
async def start_wf(request: StartWorkflowRequest):
    return WorkflowResponse(correlation_id = request.correlation_id, namespace = request.namespace, status = "In Progress")

@router.post("/topology", response_model=WorkflowResponse)
async def start_topology_wf(request: Topology):
    return WorkflowResponse(correlation_id = '', namespace = request.namespace, status = "In Progress")
