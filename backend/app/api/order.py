from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class OrderCreate(BaseModel):
    user_id: int
    symbol: str
    quantity: int
    side: str  # "buy" or "sell"

class OrderResponse(BaseModel):
    order_id: int
    status: str

@router.post("/", response_model=OrderResponse)
async def create_order(order: OrderCreate):
    # Core logic will be in service
    from ..services.order_service import process_order
    result = await process_order(order)
    return result

@router.get("/", response_model=List[OrderResponse])
async def list_orders():
    # Placeholder
    return []
