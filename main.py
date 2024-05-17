import uvicorn
from fastapi import FastAPI
from models import User


app = FastAPI()

# создаём модель данных, которая обычно расположена в файле models.py
# Внешние данные, имитирует входящий JSON
external_data = {'id': '800',
                 'signup': '2017-06-01 12:22',
                 'name': 'lolita',
                 'friends': [1, 2, 3]}

# имитируем распаковку входящих данных в коде приложения
user = User(**external_data)
print(user)

if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
