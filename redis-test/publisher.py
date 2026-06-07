from db import get_redis


async def publish(msg: str):
    r = get_redis()
    await r.publish("publish", msg)
    await r.close()
