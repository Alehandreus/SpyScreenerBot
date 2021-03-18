from pynput import keyboard
import pyautogui
from settings import chat_id, token, send_screenshot_hotkeys, stop_hotkeys, send_text_hotkeys
import telebot
import os
from time import sleep


bot = telebot.AsyncTeleBot(token)

print("Working...")

current = set()


def on_press(key):
    current.add(key)
    try:
        for hotkey in send_screenshot_hotkeys:
            if all(k in current for k in hotkey):
                make_screenshot()
                with open("screenshot.png", "rb") as photo:
                    bot.send_document(chat_id, photo)
                    sleep(0.1)
                    print("Screenshot sent")
                delete_screenshot()

        for hotkey in stop_hotkeys:
            if all(k in current for k in hotkey):
                keyboard_listener.stop()
                print("Process stopped")

        for hotkey, text in send_text_hotkeys.items():
            if all(k in current for k in hotkey):
                bot.send_message(chat_id, text)
                print("Message sent")

    except Exception as ex:
        print("ex")
        print(ex)


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


def make_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')


def delete_screenshot():
    try:
        os.remove('screenshot.png')
    except Exception as ex:
        print(ex)


def get_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    photo = open('screenshot.png', 'rb')
    return photo


with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
    keyboard_listener.join()
