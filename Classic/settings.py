from pynput import keyboard


# str
token = ""

# list of ints
chat_ids = [

]

# send types:
#   new: more clean but in telegram doesnt recognize screenshot like photo. Preview works fine
#   old: its quite a dirty way, but everything works fine
photo_send_type = "old"

send_screenshot_hotkeys = [
    [keyboard.Key.shift_r]
]

stop_hotkeys = [
    [keyboard.Key.pause],
    [keyboard.Key.shift, keyboard.KeyCode(char='C')]
]

send_text_hotkeys = {
    (keyboard.Key.shift, keyboard.KeyCode(char='!')): "Hello",
    (keyboard.Key.shift, keyboard.KeyCode(char='@')): "Cya",
}
