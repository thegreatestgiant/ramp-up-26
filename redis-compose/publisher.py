from db import get_redis


def publish(msg: str):
    r = get_redis()
    r.publish("publish", msg)
    r.close()
