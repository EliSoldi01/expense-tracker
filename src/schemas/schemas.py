
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionCreate(BaseModel):
    type: TransactionType
    date: date
    amount: float = Field(..., gt=0) # > 0
    category: str
    description: Optional[str] = None

class TransactionUpdate(BaseModel):
    type: Optional[TransactionType]
    date: Optional[date]
    amount: Optional[float]
    category: Optional[str]
    description: Optional[str]