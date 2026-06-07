import asyncio

import redis
from db import get_redis


async def start_subscriber():
    r = get_redis()
    pubsub = r.pubsub()
    await pubsub.subscribe("publish")

    print("Starting to listen")
    while True:
        try:
            async for msg in pubsub.listen():
                if msg["type"] == "message":
                    print(f"data: {msg['data']}")
        except redis.ConnectionError:
            print("Connection lost, reconnecting...")
            await asyncio.sleep(2)
            await pubsub.subscribe("publish")
            print("Reconnected")
        except Exception as e:
            print(f"Error is {e}")
            break
