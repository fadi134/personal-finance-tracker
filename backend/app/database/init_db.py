from app.database.connection import engine
from app.database.base import Base

# Import all models here
from app.models.transaction import Transaction


def create_tables():
    Base.metadata.create_all(bind=engine)