from db import get_redis


def start_subscriber():
    r = get_redis()
    pubsub = r.pubsub()
    pubsub.subscribe("publish")

    print("Starting to listen")
    try:
        for msg in pubsub.listen():
            if msg["type"] == "message":
                print(f"data: {msg['data']}")
    finally:
        pubsub.unsubscribe("publish")
        r.close()


if __name__ == "__main__":
    start_subscriber()
