import redis.asyncio as redis

pool = redis.ConnectionPool(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True,
    health_check_interval=30,
    socket_timeout=None,
)


def get_redis():
    return redis.Redis(connection_pool=pool)
