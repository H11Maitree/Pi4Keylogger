# Server
This is the Web Server module for the interaction beetween Hacker client device (To see what being type and to inject typing in from Web page). The main routes is in [app.py](./app.py). The defult running will run on `0.0.0.0` (default web server for using in the local network). 

The `Web Server` will distribute HTML and those HTML will communicate back with the Flask server using `Socket.IO`

### Routes
| Route  | Descriptions |
| ------------- | ------------- |
| `/`  | For observing live key-stoke |
| `/control`  | For injecting text into the target computer |

### Socket (`SockketIO`)
| Chennel  | Descriptions |
| ------------- | ------------- |
| `keylogger`  | For broadcasting the live key-stoke from server to client |
| `injector`  | For handeling injecting text from client to server |

## Run
This command will run the `Web Server` module
```bash
# @ Pi4Keylogger %
python3 -m Server.app
```