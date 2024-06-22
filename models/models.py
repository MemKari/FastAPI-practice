from typing import AsyncGenerator, Optional

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import EmailStr
from sqlalchemy import String, ForeignKey, DateTime, Float
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

'''Переменная metadata действительно не нужна в вашем коде, так как вы используете декларативный стиль 
определения моделей с помощью SQLAlchemy ORM, который сам управляет метаданными. Убедитесь, 
что вы вызываете Base.metadata.create_all(engine) вместо metadata.create_all(engine) для создания таблиц.'''

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    ...


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(30))
    degree: Mapped[Optional[str]] = mapped_column(String(60), nullable=True)
    email: Mapped[EmailStr] = mapped_column(String(50), unique=True, nullable=False)
    registered_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, role={self.role!r})"


class Trade(Base):
    __tablename__ = 'trade'

    trade_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    currency: Mapped[str] = mapped_column(String(15))
    side: Mapped[str] = mapped_column(String(15))
    price: Mapped[float] = mapped_column(Float)
    amount: Mapped[float] = mapped_column(Float)

    def __repr__(self) -> str:
        return (f"Trade(trade_id={self.trade_id!r}, user_id={self.user_id!r}, currency={self.currency!r}, "
                f"side={self.side!r}, price={self.price!r}, amount={self.amount!r})")


# Создание таблиц в базе данных.
metadata = Base.metadata



engine = create_async_engine(DATABASE_URL)  # точка входа sql алхимии в приложение
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
