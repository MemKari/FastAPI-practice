import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("index.html")


@app.post('/calculate')  # an example of post request: http://127.0.0.1/calculate?num1=5&num2=10
def calculate(num1: int, num2: int):
    return {"result": num1 + num2}


if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
