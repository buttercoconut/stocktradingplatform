"""Pydantic models for request/response schemas.

These models are used by the API layer to validate input and shape output.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Stock schemas
class StockBase(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=5)
    name: str

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Order schemas
class OrderBase(BaseModel):
    user_id: int
    stock_id: int
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    order_type: str = Field(..., regex="^(buy|sell)$")

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
