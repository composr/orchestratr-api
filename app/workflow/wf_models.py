from pydantic import BaseModel, ValidationError

class StartWorkflowRequest(BaseModel):
    namespace: str = None
    correlation_id: str = None

class WorkflowResponse(BaseModel):
    namespace: str = None
    status: str = None
    correlation_id: str = None