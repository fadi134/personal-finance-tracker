from datetime import date
from typing import Optional
from app.constants.transaction_type import TransactionType
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class TransactionType(str, Enum):
    INCOME = "Income"
    EXPENSE = "Expense"

class TransactionCreate(BaseModel):
    date: date
    description: str = Field(..., min_length=1, max_length=255)
    amount: float = Field(..., gt=0)
    transaction_type: TransactionType
    category: Optional[str] = None
    source: Optional[str] = "Manual"


class TransactionUpdate(BaseModel):
    date: Optional[date] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    transaction_type: TransactionType
    category: Optional[str] = None
    source: Optional[str] = None


class TransactionResponse(BaseModel):
    id: int
    date: date
    description: str
    amount: float
    transaction_type: str
    category: Optional[str] = None
    source: str

    model_config = ConfigDict(from_attributes=True)