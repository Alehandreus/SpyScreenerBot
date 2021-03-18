from pynput import keyboard
from CentralManager import CentralManager
from settings import chat_id, token


central_manager = CentralManager(chat_id, token)


def on_press(key):
    print(key)
    try:
        if key == keyboard.Key.alt_gr:
            central_manager.switch_command_up()
        elif key == keyboard.Key.ctrl_r:
            central_manager.execute_command()
        elif key == keyboard.Key.pause:
            central_manager.blink()
    except Exception as ex:
        print("ex")
        print(ex)


with keyboard.Listener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()
