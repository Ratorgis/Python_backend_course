from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str

@app.get("/hello")
def hello_world() -> str:
    return "world!"

@app.post('/info')
def output_json() -> User:
    return User(10, 'Max')
