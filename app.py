from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    "Главная страница со списком доступных эндпоинтов"
    endpoints = {
        "Главная страница": "/",
        "Приветствие": {
            "url": "/greet/",
            "params": {"name": "строка (например, Maksim)"},
            "example": "/greet/?name=Maksim"
        },
        "Калькулятор": {
            "url": "/calculate/",
            "params": {"a": "число", "b": "число"},
            "example": "/calculate/?a=2&b=3"
        }
    }
    return endpoints

@app.get("/{name}")
def read_root():
    return {"Hello": "World"}

@app.get("/greet/")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/calculatings/")
def cal(a: int, b: int):
    return f"{a} + {b} = {a + b}"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
