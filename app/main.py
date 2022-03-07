from fastapi import Depends, FastAPI, Header, HTTPException
from app.liveness import liveness
from app.workflow import wf_router

app = FastAPI(
    title="Orchestratr API",
    description="An API wrapper atop an underlying execution engine, in this case Prefect",
    version="0.1",
)

app.include_router(liveness.router, prefix="/liveness")
app.include_router(wf_router.router, prefix="/workflow")