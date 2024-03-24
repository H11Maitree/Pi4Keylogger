# Pi4Keylogger

A hands-on project using `Raspberry Pi 4B` to explore **keylogging mechanics** (as a `Keylogger`). 

Designed for educational use, this project emphasizes `USB device emulation` (`HID`) and keystroke capture.

---

***Disclaimer:** The creation and use of a keylogger for malicious purposes are unethical and illegal.*

*The information provided in this repository is meant for educational purposes only. This repository was made to showcase how it can be created with technical processes, to help understand how to protect against them, and to showcase Raspberry Pi's capabilities in cybersecurity.*

## Hardware
This project was build and tested in `Raspberry Pi model 4B`

However every `Raspberry Pi` that support `USB On-To-Go` (e.g. `pico`, `zero`, `400`, `4B`; note that `3B+` is not support USB OTG) should beable to benefit from this set-up as well.

Per usage, you need to have:
- Keyboard 
- USB-C (plug to Pi) to USB-A/C (plug to the target computer), power and data cable

Per Debuging/Deverloping, you need to have:
- Monitor
- Mouse

## Setup
On you Raspberry Pi, make sure that you complete these set-up

### OS
**Debian version:** [11 (bullseye)](https://downloads.raspberrypi.com/raspios_oldstable_arm64/images/?_gl=1*jurfy8*_ga*ODg1ODc5MTg0LjE3MDk5OTQ1Nzg.*_ga_22FD70LWDS*MTcxMTI3MTQ1NS4xLjEuMTcxMTI3MTUyOC4wLjAuMA..)

### Activate HID Gadget mode 
Please follow the activation process to enable `dev/hidg0` for simulating the USB interface at [zero-hid](https://github.com/thewh1teagle/zero-hid/tree/main/usb_gadget#usb-gadget-module-configuration-for-zero-hid) documantation.

Upon successful activation you should see `dev/hidg0` when explore the file (e.g. via `File Explorer`)

### Python Library to Install
- [zero-hid](https://pypi.org/project/zero-hid/)
- [keyboard]()
- [flask](https://pypi.org/project/flask/)
- [flask_socketio](https://pypi.org/project/flask_socketio/)
- [eventlet](https://pypi.org/project/eventlet/)
- [redis](https://pypi.org/project/redis/)

### Redis Daemon
Dowload Redis from the [official site](https://redis.io/download/)

You should beable to start the Redis Deamon by:
```bash
sudo systemctl start redis
```


## Getting Started
1. Get into the project Directory
```bash
cd ~/PATH/Pi4KeyLogger
```
2. Run Logger module
```
# @ ~/PATH/Pi4KeyLogger %
sudo python3 -m Logger.main
```
3. Run Server module
```
# @ ~/PATH/Pi4KeyLogger %
python3 -m Server.app
```

NOTE: The Server and Logger should be run in the different process (e.g. New Terminal per each `python3` command)
