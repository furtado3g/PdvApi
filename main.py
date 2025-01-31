import bcrypt
from fastapi import FastAPI
from prisma import Prisma
from src.adapters.Repositories.UserRepository import UserRepository

from src.application.use_cases.UserUseCases import UserUseCases
from src.domain.Entities.User import User

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
    use_cases = UserUseCases(prisma)
    return await use_cases.get_all_users()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    use_cases = UserUseCases(prisma)
    return await use_cases.get_user(user_id)


@app.post("/users")
async def create_user(data: dict):
    await prisma.connect()
    user = User(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        street=data["street"],
        zipcode=data["zipcode"],
        house_no=data["house_no"],
        complement=data["complement"],
        city=data["city"],
        state=data["state"],
        country=data["country"],
        username=data["username"],
        password= bcrypt.hashpw(data["password"].encode('utf-8'), salt=bcrypt.gensalt()).decode("utf-8"),
        role=data["role"],
        is_active=data["is_active"],
        is_admin=data["is_admin"],
    )
    repository = UserRepository(prisma)
    created = await UserUseCases(repository).create_user(user.to_insert())
    await prisma.disconnect()
    return created
