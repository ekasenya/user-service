from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hi there"}


@app.get('/health')
async def check_health():
    return {"status": "OK"}