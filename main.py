from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from internal import admin
from routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}