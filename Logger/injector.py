from Logger.utils.redis_worker import receive
from zero_hid import Keyboard

def callback(data):

    # Print out reciving data for debuging
    print("Callback: ", data)

    # Attract the command e.g. "type"
    action = data['command']

    # Attract the Target value e.g. "THIS IS THE INJECT STRING"
    val = data['val']

    if(action == "type"):
        # If command is to "type"
        with Keyboard() as k:
            # ask HID to type the value in
            k.type(val)


def start():
    # Sending the callback to bind with Redis
    receive(callback)

if __name__ == '__main__':
    start()