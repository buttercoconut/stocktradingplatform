from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter()

@router.get("/", response_model=list)
async def list_stocks():
    return [
        {"symbol": "AAPL", "name": "Apple Inc.", "price": 150.0, "last_updated": datetime.utcnow()},
        {"symbol": "GOOG", "name": "Alphabet Inc.", "price": 2800.0, "last_updated": datetime.utcnow()},
    ]
