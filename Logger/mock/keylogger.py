import threading
from Logger.utils.redis_worker import send

def execute(thread_event):
    mock_data = {'action':'press', 'key':'a'}
    print("Keylogger mock Sending: ", mock_data)
    send(mock_data)
    if not thread_event.is_set():
        # call execute() again in 5 seconds
        threading.Timer(5, execute, [thread_event]).start()

def start():
    event = threading.Event()
    execute(event) 

if __name__ == '__main__':
    start()
