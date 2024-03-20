from Logger.utils.redis_worker import receive
from zero_hid import Keyboard

def callback(data):
    print("DEBUG", data)
    action = data['command']
    val = data['val']
    if(action == "type"):
        with Keyboard() as k:
            k.type(val)


def start():
    receive(callback)

if __name__ == '__main__':
    start()