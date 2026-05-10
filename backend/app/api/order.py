# backend/app/api/order.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/")
def place_order(user_id: int, stock_symbol: str, quantity: int, side: str, db: Session = Depends(get_db)):
    service = OrderService(db)
    try:
        order = service.place_order(user_id, stock_symbol, quantity, side)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return order
