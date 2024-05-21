from fastapi import APIRouter
from models import User

router = APIRouter()

# Внешние данные, имитирует входящий JSON
new_user = User(id = 1, name ='default user')

''' Реализуйте функцию, которая при получении GET-запроса по дополнительному маршруту `/users` возвращала бы JSON с данными о пользователе (юзере).
'''


@router.get('/users', response_model=User)
async def get_user():
    return new_user