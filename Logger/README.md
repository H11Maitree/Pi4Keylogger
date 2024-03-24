# Logger
This is the module for the interaction beetween physical devices (USB that conect to the target device, and Keyboard input of the Pi), Combining two part [keylogger](./keylogger.py), [injector](./injector.py).

### keylogger
This module wil forward the Keyboard stroke event (`Press`/`Release`) -> `Redis Sub/Pub`, along with simulating the stoke to the USB as a `KeyCode` to the target computer.

### injector
This module wil wait to recive typing request from the Web Server from `Redis Sub/Pub`, mainly to inject some string to simulate remote typing.

## Run
This command will run the `Logger` module
```bash
# @ Pi4Keylogger %
sudo python3 -m Logger.main
```