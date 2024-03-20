import keyboard
from zero_hid import Keyboard
from zero_hid import KeyCodes as c

m = {
    1: c.KEY_ESC,
    #first row
    2: c.KEY_1,
    3: c.KEY_2,
    4: c.KEY_3,
    5: c.KEY_4,
    6: c.KEY_5,
    7: c.KEY_6,
    8: c.KEY_7,
    9: c.KEY_8,
    10: c.KEY_9,
    11: c.KEY_0,
    12: c.KEY_MINUS,
    13: c.KEY_EQUAL,
    
    #second row
    16: c.KEY_Q,
    17: c.KEY_W,
    18: c.KEY_E,
    19: c.KEY_R,
    20: c.KEY_T,
    21: c.KEY_Y,
    22: c.KEY_U,
    23: c.KEY_I,
    24: c.KEY_O,
    25: c.KEY_P,
    26: c.KEY_LEFTBRACE,
    27: c.KEY_RIGHTBRACE,
    
    #third row
    30: c.KEY_A,
    31: c.KEY_S,
    32: c.KEY_D,
    33: c.KEY_F,
    34: c.KEY_G,
    35: c.KEY_H,
    36: c.KEY_J,
    37: c.KEY_K,
    38: c.KEY_L,
    39: c.KEY_SEMICOLON,
    40: c.KEY_APOSTROPHE,
    41: c.KEY_GRAVE,
    43: c.KEY_BACKSLASH,
    
    #fourth row
    44: c.KEY_Z,
    45: c.KEY_X,
    46: c.KEY_C,
    47: c.KEY_V,
    48: c.KEY_B,
    49: c.KEY_N,
    50: c.KEY_M,
    51: c.KEY_COMMA,
    52: c.KEY_DOT,
    53: c.KEY_SLASH,
    59: c.KEY_F1,
    60: c.KEY_F2,
    61: c.KEY_F3,
    62: c.KEY_F4,
    63: c.KEY_F5,
    64: c.KEY_F6,
    65: c.KEY_F7,
    66: c.KEY_F8,
    67: c.KEY_F9,
    68: c.KEY_F10,
    87: c.KEY_F11,
    88: c.KEY_F12,
    
    
    14: c.KEY_BACKSPACE,
    15: c.KEY_TAB,
    28: c.KEY_ENTER,
    29: c.MOD_LEFT_CONTROL,
    42: c.MOD_LEFT_SHIFT,
    
    
    54: c.MOD_RIGHT_SHIFT,
    55: c.KEY_KPASTERISK,
    56: c.MOD_LEFT_ALT,
    57: c.KEY_SPACE,
    58: c.KEY_CAPSLOCK,
    
    # num lock
    69: c.KEY_NUMLOCK,
    70: c.KEY_SCROLLLOCK,
    71: c.KEY_KP7,
    72: c.KEY_KP8,
    73: c.KEY_KP9,
    74: c.KEY_KPMINUS,
    75: c.KEY_KP4,
    76: c.KEY_KP5,
    77: c.KEY_KP6,
    78: c.KEY_KPPLUS,
    79: c.KEY_KP1,
    80: c.KEY_KP2,
    81: c.KEY_KP3,
    82: c.KEY_KP0,
    83: c.KEY_KPDOT,
    
    96: c.KEY_KPENTER,
    97: c.MOD_RIGHT_CONTROL,
    98: c.KEY_KPSLASH,
    99: c.KEY_SYSRQ,
    100: c.MOD_RIGHT_ALT,
    
    102: c.KEY_HOME,
    103: c.KEY_UP,
    104: c.KEY_PAGEUP,
    105: c.KEY_LEFT,
    106: c.KEY_RIGHT,
    107: c.KEY_END,
    108: c.KEY_DOWN,
    109: c.KEY_PAGEDOWN,
    110: c.KEY_INSERT,
    111: c.KEY_DELETE,
    
    119: c.KEY_PAUSE,
    125: c.MOD_LEFT_GUI,
    126: c.MOD_RIGHT_GUI,
}

modifier = {
    42, #c.MOD_LEFT_SHIFT,
    54, #c.MOD_RIGHT_SHIFT,
    29, #c.MOD_LEFT_CONTROL,
    97, #c.MOD_RIGHT_CONTROL,
    56, #c.MOD_LEFT_ALT,
    100, #c.MOD_RIGHT_ALT,
    125, #c.MOD_LEFT_GUI,
    126, #c.MOD_RIGHT_GUI,
}

current_applied_modifier = set()

def event_hook(event):
    with Keyboard() as k:
        keycode = m[event.scan_code]
        is_modifier = (event.scan_code in modifier)
        if event.event_type == keyboard.KEY_DOWN:
            print("PRESS: ",event.scan_code,keycode)
            if is_modifier:
                current_applied_modifier.add(keycode)
            else:
                k.press(list(current_applied_modifier), m[event.scan_code], release=False)
        else:
            if is_modifier:
                current_applied_modifier.remove(keycode)
            else:
                k.release()

keyboard.hook(event_hook)
keyboard.wait()
