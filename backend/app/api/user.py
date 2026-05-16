from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class User(BaseModel):
    id: int
    username: str

# Dummy dependency for auth
async def get_current_user() -> User:
    return User(id=1, username="demo")

@router.get("/me", response_model=User)
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user
