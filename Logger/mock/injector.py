from Logger.utils.redis_worker import receive

def callback(data):
    # Print out data the recived from the Redis
    print("Recived: ", data)
def start():
    # Sending the Callback function for redis receive module to attrach as a listiner
    receive(callback)

if __name__ == '__main__':
    # If running this file directly, start the injector mocking
    start()