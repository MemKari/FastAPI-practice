from fastapi import FastAPI
import uvicorn
import routes

app = FastAPI(title='Tradind App')
app.include_router(routes.router)

if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
