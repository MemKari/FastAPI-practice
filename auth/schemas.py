from datetime import datetime

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    role: str
    degree: str
    role_id: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    id: int
    name: str
    hashed_password: str
    email: EmailStr
    role: str
    degree: str
    registered_at: datetime
    role_id: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserUpdate(schemas.BaseUserUpdate):
    pass
