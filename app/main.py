from fastapi import Depends, FastAPI, Header, HTTPException
from .api.routers import liveness

app = FastAPI(
    title="FastApi Skeleton",
    description="A Boilerplate FastApi project",
    version="1.0",
)

app.include_router(liveness.router, prefix="/liveness")
