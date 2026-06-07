from fastapi import FastAPI
from publisher import publish

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     task = asyncio.create_task(start_subscriber())
#     yield
#     task.cancel()


# app = FastAPI(lifespan=lifespan)
app = FastAPI()


@app.post("/publish")
def publisher(msg: str):
    publish(msg)
