from pydantic import BaseModel

# создаём модель данных, которая обычно расположена в файле models.py

class User(BaseModel):
    id: int
    name: str
