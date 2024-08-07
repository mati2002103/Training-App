from fastapi import FastAPI,HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Model danych dla żądania logowania
class LoginRequest(BaseModel):
    login: str
    password: str

# Przykładowa baza danych użytkowników
users_db = {
    "user1": "password123",
    "user2": "password456",
}


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# Przykładowa baza danych użytkowników
users_db = {
    "user1": "password123",
    "user2": "password456",
}


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your training app."}

@app.get("/login_page", tags=["login"])
async def login_page() -> dict:
    return { "data": users_db }


@app.post("/login")
async def login(request: LoginRequest) -> Dict[str, str]:
    if request.login in users_db and users_db[request.login] == request.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid login or password")