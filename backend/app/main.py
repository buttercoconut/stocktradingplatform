# backend/app/main.py
from fastapi import FastAPI
from .api.user import router as user_router
from .api.stock import router as stock_router
from .api.order import router as order_router

app = FastAPI(title="Stock Trading Platform API")

app.include_router(user_router)
app.include_router(stock_router)
app.include_router(order_router)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    from .database import Base, engine
    Base.metadata.create_all(bind=engine)
