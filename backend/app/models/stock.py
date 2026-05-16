from pydantic import BaseModel

class Stock(BaseModel):
    symbol: str
    name: str
    exchange: str
    current_price: float
    change_percent: float
