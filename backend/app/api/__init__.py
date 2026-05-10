from fastapi import APIRouter
from . import user, stock, order

router = APIRouter()
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(stock.router, prefix="/stocks", tags=["stocks"])
router.include_router(order.router, prefix="/orders", tags=["orders"])
