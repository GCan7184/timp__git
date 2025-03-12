from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/World")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_greet():
    response = client.get("/greet/", params={"name": "Alice"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice!"}

def test_calculate():
    response = client.get("/calculatings/", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.text == '"2 + 3 = 5"'
