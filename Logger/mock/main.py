import threading
from Logger.mock import injector, keylogger

def start():
    keylogger_thread = threading.Thread(target=keylogger.start)

    # Start mocked Keylogger module
    keylogger_thread.start()

    # Start mocked Injector module 
    injector.start()

if __name__ == '__main__':
    start()

