from pydantic import BaseModel, ValidationError
from typing import List, Dict, Any

class TopologyNode(BaseModel):
    id: str
    node_type: str
    properties: Dict[Any, Any]

class Topology(BaseModel):
    id: str
    name: str
    namespace: str
    blueprint: str
    version: str
    nodes: List[TopologyNode]

    