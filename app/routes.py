from typing import List, Annotated
from pydantic import EmailStr
from fastapi import APIRouter, File, UploadFile, Path, Query
from models import User, Trade, Degree
from databases import fake_users, fake_trades

router = APIRouter()


@router.get('/get_user/{user_id}')
async def getting_user(
        user_id: Annotated[int, Path(title="User's Id for getting User")]):
    '''Точно так же, как вы можете объявить дополнительные проверки и метаданные для параметров запроса с помощью Query,
     вы можете объявить тот же тип проверок и метаданных для параметров пути с помощью Path.'''
    return [user for user in fake_users if user.get('id') == user_id][0]


@router.get('/all_users')
async def get_all_users(limit: Annotated[int, Query(title='Count of users you will get', ge=1,le=10)] = 5):
    users_in_limit = fake_users[:limit]
    return users_in_limit


@router.post('/new_account', response_model=User)
async def create_new_user(degree: Degree, id: int, name: str, email: EmailStr, role: str = 'trader', ):
    new_user = User(id=id, name=name, role=role, degree=degree, email=email)
    fake_users.extend(new_user)
    return new_user


@router.post('/trades')
async def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'result': 'Trades added successfully'}


@router.post('/files')
async def add_file(
        file: Annotated[bytes, File(description='to set metadata')]):  # File загружает только содержимое файла,
    return {'File was processed. File size:': len(file)}


@router.post('/upload_file')
async def add_file_with_metadate(
        upload_file: UploadFile):  # UploadFile загружает метаинформацию вместе с самим содержимым
    return {'File was processed. File name:': upload_file.filename}
