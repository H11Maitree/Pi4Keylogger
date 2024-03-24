# Mock Logger
This is the mock module for Logger, using when debuging the web server, when running this module it:
- Will send out message to redis sub/pub `keylogger` simulating pressing `PRESS A` every 5 seconds; [injector.py](./injector.py)
```json
{
	'action':'PRESS', 
	'scan_code':30
}
```
- Will print out the message recive from injecting redis sub/pub `injector` chennel; [keylogger.py](./keylogger.py)

## Run
This command will run the mock module
```bash
# @ Pi4Keylogger %
sudo python3 -m Logger.mock.main
```