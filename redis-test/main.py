from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from redis import Redis


# TODO: Figure out how to open and close db on open and close
# @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = Redis()
    app.state.http_client = httpx.AsyncClient
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/listen")
async def lister():
    value = app.state.redis.get("listen")
    if value is None:
        response = await app.state.client.http_client.get()
        return response.json()
