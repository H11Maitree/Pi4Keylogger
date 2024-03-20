from Logger.utils.redis_worker import receive

def callback(data):
    print("Recived: ", data)
def start():
    receive(callback)

if __name__ == '__main__':
    start()