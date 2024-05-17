from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    signup: Union[datetime, None] = None
    friends: List[int]=[]


