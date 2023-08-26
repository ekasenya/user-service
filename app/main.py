import os

import uvicorn
from fastapi import FastAPI, Depends

from app.core.deps import get_user_repository
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserInfo, User

app = FastAPI()


config = {
    'DB_NAME': os.environ.get('DB_NAME', 'user-db'),
    'DB_HOST': os.environ['DB_HOST'],
    'DB_PORT': os.environ['DB_PORT'],
    'GREETING': os.environ.get('GREETING', 'Hello'),
}


@app.get('/')
async def root():
    return {"message": "Hi there"}


@app.get('/health')
async def check_health():
    return {"status": "OK"}


@app.post('/user', response_model=User)
async def create_user(user_info: UserInfo, user_repository: UserRepository = Depends(get_user_repository)):
    return await user_repository.create_user(name=user_info.name, email=user_info.email)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")