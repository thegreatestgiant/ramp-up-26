import asyncio
from contextlib import asynccontextmanager

import redis
from fastapi import FastAPI
from publisher import publish
from subscriber import start_subscriber

pool = redis.ConnectionPool(host="localhost", port=6379, db=0)


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(start_subscriber())
    yield
    task.cancel()


app = FastAPI(lifespan=lifespan)


@app.post("/publish")
async def publisher(msg: str):
    await publish(msg)
