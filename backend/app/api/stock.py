from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

router = APIRouter()

class StockInfo(BaseModel):
    symbol: str
    price: float

@router.get("/", response_model=List[StockInfo])
async def list_stocks():
    # Placeholder: return static list
    return [StockInfo(symbol="AAPL", price=150.0), StockInfo(symbol="GOOG", price=2800.0)]
