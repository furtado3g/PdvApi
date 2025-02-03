import bcrypt,jwt
from fastapi import FastAPI
from prisma import Prisma
from src.Models import UserData, LoginData

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

prisma = Prisma()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users")
async def get_users():
    pass


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    None


@app.post("/users")
async def create_user(data: UserData):
    await prisma.connect()
    user = {
        'name': data["name"],
        'email': data["email"],
        'phone': data["phone"],
        'street': data["street"],
        'zipcode': data["zipcode"],
        'house_no': data["house_no"],
        'complement': None if "complement" not in data else data["complement"],
        'city': data["city"],
        'state': data["state"],
        'country': data["country"],
        'username': data["username"],
        'password': bcrypt.hashpw(data["password"].encode('utf-8'), salt=bcrypt.gensalt()).decode("utf-8"),
        'role': data["role"],
        'is_active': data["is_active"],
        'is_admin': data["is_admin"],
    }
    if await prisma.user.find_unique(where={
        "username": user["username"]
    }):
        await prisma.disconnect()
        return {
            "status": "error",
            "message": "Nome de usuário já esta em uso!"
        }, 403
    elif await prisma.user.find_unique(where={
        "email": user["email"]
    }):
        await prisma.disconnect()
        return {
            "status": "error",
            "message": "Email já esta em uso!"
        }, 403
    else:
        r = await prisma.user.create(data=user)
        await prisma.disconnect()
        return r, 200


@app.post("/auth/login")
async def login(data: LoginData):
    d = data.dict()
    await prisma.connect()
    user = await prisma.user.find_first(where={
        'username': d["username"]
    }
    )
    if not user:
        return {
            "status": "error",
            "message": "Usuário não encontrado!"
        }
    if bcrypt.checkpw(d["password"].encode('utf-8'), user.password.encode('utf-8')):
        return {
            "token": ""
        }
    else:
        return {
            "status": "error",
            "message": "Senha incorreta!"
        }

    return user
