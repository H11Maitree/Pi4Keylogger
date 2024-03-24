# Utils
This is the utility module for this project, which contains these sub-modules for deverlopment convenients:

| File  | Functions | Descriptions |
| ------------- | ------------- | ------------- |
| [./converter.py](./converter.py)  | `isModifier(ScanCode)`, `getKeyCode(ScanCode)`  | Converting `Linux's ScanCode` -> `USB's KeyCode`  |
| [./getIP.py](./getIP.py)  | `getIP()`  | Retuning current Device private IP in the network  |
| [./mapping.py](./mapping.py)  | -  | Keeping mapping `Linux's ScanCode` -> `USB's KeyCode` for converter |
| [./redis_worker.py](./redis_worker.py)  | `send(event)`, `receive(callback)`  | Simplify Sending and Reciving for Keylogger and Injector  |