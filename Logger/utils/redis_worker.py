import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def send(event):
    """
    Publishes an event to a specified Redis channel.

    Args:
    - event (dict): A dictionary containing the event data.
    """
    channel = 'keylogger'
    json_data = json.dumps(event)
    redis_client.publish(channel, json_data)

def receive(callback):
    """
    Subscribes to a Redis channel and listens for messages.
    The callback function is called when a message is received.
    """
    channel = 'injector'
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)

    print(f"Subscribed to {channel}, waiting for messages...")
    while True:
        message = pubsub.get_message()
        if message and message['type'] == 'message':
            # Process the message here
            event_data = json.loads(message['data'])
            callback(event_data)