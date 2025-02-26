from fastapi import FastAPI
import uvicorn

app = FastAPI()

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