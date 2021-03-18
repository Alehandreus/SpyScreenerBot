from pynput import keyboard


token = None  # str

chat_id = None  # int

send_screenshot_hotkeys = [
    [keyboard.Key.shift_r]
]

stop_hotkeys = [
    [keyboard.Key.pause],
    [keyboard.Key.shift, keyboard.KeyCode(char='C')]
]

send_text_hotkeys = {
    (keyboard.Key.shift, keyboard.KeyCode(char='!')): "Привет",
    (keyboard.Key.shift, keyboard.KeyCode(char='@')): "Пока",
}

