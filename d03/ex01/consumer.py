import json
import redis
import time
import sys


def handel_message(message: dict, sender_id):
    if (message["metadata"]["to"] == int(sender_id)) & (message["amount"] >= 0):
        print("I'm here")
        new_message = {"metadata": {"from": sender_id, "to": message["metadata"]["from"]},
                       "amount": message["amount"]}
        return new_message
    return message


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong arguments!")
        exit(1)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    p = r.pubsub()
    p.subscribe("Cash_Flow")

    while True:
        message = p.get_message()
        if message:
            if message['data'] != 1:
                mess = json.loads(message['data'])
                print(handel_message(mess, sys.argv[2].split(sep=",")[0]))
        time.sleep(1)
