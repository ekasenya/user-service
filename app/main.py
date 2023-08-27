import os

import uvicorn
from fastapi import FastAPI, Depends, status, Response
from sqlalchemy.exc import IntegrityError

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


@app.post('/user', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_info: UserInfo,
        response: Response,
        user_repository: UserRepository = Depends(get_user_repository),
):
    try:
        return await user_repository.create_user(
            user_name=user_info.user_name,
            first_name=user_info.first_name,
            last_name=user_info.last_name,
            email=user_info.email
        )
    except IntegrityError:
        response.status_code = status.HTTP_409_CONFLICT


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")