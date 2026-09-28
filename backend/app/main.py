from fastapi import FastAPI
from app.exceptions.handlers import register_exception_handlers
from app.database.init_db import create_tables
from app.api.routes import (
    transactions,
    import_routes,
)

app = FastAPI(
    title="Personal Finance Tracker",
    version="1.0.0"
)

create_tables()

app.include_router(transactions.router)
app.include_router(import_routes.router)
register_exception_handlers(app)


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }