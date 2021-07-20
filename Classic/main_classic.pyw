from pynput import keyboard
import pyautogui
from settings import chat_ids, token, send_screenshot_hotkeys, stop_hotkeys, send_text_hotkeys, photo_send_type
import telebot
import os
from time import sleep
import io


class CustomBot:
    def __init__(self, token, chat_ids):
        self.bot = telebot.AsyncTeleBot(token)
        self.chat_ids = chat_ids

    def send_document(self, document):
        for chat_id in self.chat_ids:
            self.bot.send_document(chat_id, document)
            sleep(0.1)

    def send_text(self, text):
        for chat_id in self.chat_ids:
            self.bot.send_message(chat_id, text)


bot = CustomBot(token, chat_ids)
current = set()
print("Working...")


def is_hotkey_active(hotkey_list):
    for hotkey in hotkey_list:
        if all(k in current for k in hotkey):
            return True
    return False


def on_press(key):
    current.add(key)
    try:
        if is_hotkey_active(send_screenshot_hotkeys):
            if photo_send_type == "new":
                im = pyautogui.screenshot()
                buf = io.BytesIO()
                im.save(buf, format='PNG')
                byte_im = buf.getvalue()
                bot.send_document(byte_im)
                print("Screenshot sent")

            elif photo_send_type == "old":
                screenshot = pyautogui.screenshot()
                screenshot.save('screenshot.png')
                with open("screenshot.png", "rb") as photo:
                    bot.send_document(photo)
                    print("Screenshot sent")
                os.remove('screenshot.png')
            current.clear()

        if is_hotkey_active(stop_hotkeys):
            keyboard_listener.stop()
            print("Process stopped")

        for hotkey, text in send_text_hotkeys.items():
            if all(k in current for k in hotkey):
                bot.send_text(text)
                print("Message sent")
                current.clear()

    except Exception as ex:
        print(ex)


def on_release(key):
    current.discard(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
    keyboard_listener.join()
