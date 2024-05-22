from typing import List

from fastapi import APIRouter
from models import User, Trade, Degree
from databases import fake_users, fake_trades

router = APIRouter()


@router.get('/get_user/{user_id}')
async def getting_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id][0]


@router.post('/new_account', response_model=User)
async def create_new_user(degree: Degree, id: int, name: str, role: str = 'trader', ):
    new_user = User(id=id, name=name, role=role, degree=degree)
    fake_users.extend(new_user)
    return new_user


@router.post('/trades')
async def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'result': 'Trades added successfully'}
