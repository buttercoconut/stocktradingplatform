from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter()

@router.get("/", response_model=list)
async def list_users():
    return [
        {"id": 1, "username": "alice", "email": "alice@example.com"},
        {"id": 2, "username": "bob", "email": "bob@example.com"},
    ]
