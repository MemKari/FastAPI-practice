from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, EmailStr


#  модель данных обычно расположена в файле models.py

class DegreeType(Enum):
    newbie: str = 'newbie'
    expert: str = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    name: str = Field(max_length=55)
    role: str = Field(max_length=10)
    degree: Degree
    email: EmailStr


class Trade(BaseModel):
    trade_id: int
    user_id: int
    currency: str
    side: str
    price: float = Field(ge=1)
    amount: float = Field(ge=1)
