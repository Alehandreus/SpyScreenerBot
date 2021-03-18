from pynput import keyboard


def on_press(key):
    if len(str(key)) == 3:
        res = "keyboard.KeyCode(char=" + str(key) + ")"
    else:
        res = "keyboard." + str(key)
    print(res)


with keyboard.Listener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()
