from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class OrderRequest(BaseModel):
    symbol: str
    quantity: int
    side: str

@router.post("/", response_model=dict)
async def place_order(order: OrderRequest, user_id: int = Depends(lambda: 1)):
    # Simplified order placement logic
    return {"order_id": 123, "status": "placed", "symbol": order.symbol}
