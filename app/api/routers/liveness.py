from fastapi import APIRouter, Request, Response, Body, HTTPException, Header
from fastapi.responses import PlainTextResponse


router = APIRouter()


@router.get("", status_code=200)
async def health():
    return {"Message": "i am alive"}
