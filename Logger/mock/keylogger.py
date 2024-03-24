import threading
from Logger.utils.redis_worker import send

def execute(thread_event):

    # Mock data seeding
    mock_data = {'action':'PRESS', 'scan_code':30}

    # Print out to console
    print("Keylogger mock Sending: ", mock_data)

    # Send via Redis
    send(mock_data)

    if not thread_event.is_set():
        # Create new thread to call execute() again in the next 5 seconds.
        threading.Timer(5, execute, [thread_event]).start()

def start():
    # Create the initiation first thread
    event = threading.Event()

    # Start the first thread
    execute(event) 

if __name__ == '__main__':
    start()
