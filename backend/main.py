from fastapi import FastAPI
from .api import user, stock, order

app = FastAPI(title="Stock Trading Platform API")

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(stock.router, prefix="/stocks", tags=["stocks"])
app.include_router(order.router, prefix="/orders", tags=["orders"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
