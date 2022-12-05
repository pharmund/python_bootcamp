import json
from random import randint
import redis
import time


if __name__ == "__main__":
    queue = redis.StrictRedis(host='localhost', port=6379, db=0)
    channel = queue.pubsub()

    # for i in range(5):
    #     record = {
    #         "metadata": {
    #             "from": randint(1000000000, 9999999999),
    #             "to": randint(1000000000, 9999999999)
    #         },
    #         "amount": randint(-10000, 10000)
    #     }
    #     queue.set("Cash_Flow", json.dumps(record))
    #     queue.publish("Cash_Flow", json.dumps(record))
    #     print(f"Cash_Flow: {queue.get('Cash_Flow')}")
    #     time.sleep(0.5)

    # TEST FROM SUBJECT
    r1 = {"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 10000}
    r2 = {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}
    r3 = {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}

    queue.set("Cash_Flow", json.dumps(r1))
    queue.publish("Cash_Flow", json.dumps(r1))
    print(f"Cash_Flow: {queue.get('Cash_Flow')}")
    time.sleep(0.5)
    queue.set("Cash_Flow", json.dumps(r2))
    queue.publish("Cash_Flow", json.dumps(r2))
    print(f"Cash_Flow: {queue.get('Cash_Flow')}")
    time.sleep(0.5)
    queue.set("Cash_Flow", json.dumps(r3))
    queue.publish("Cash_Flow", json.dumps(r3))
    print(f"Cash_Flow: {queue.get('Cash_Flow')}")
    time.sleep(0.5)
