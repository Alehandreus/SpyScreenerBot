from TelebotSender import TelebotSender
import pyautogui
from ChromaPython import ChromaGrid, Colors, ChromaAppInfo, ChromaApp
from time import sleep


class SendTextCommand:
    def __init__(self, x, y, text, telebot_sender):
        self.x = x
        self.y = y
        self.telebot_sender = telebot_sender
        self.text = text

    def execute(self):
        self.telebot_sender.send_text(self.text)


class SendScreenCommand:
    def __init__(self, x, y, telebot_sender):
        self.x = x
        self.y = y
        self.telebot_sender = telebot_sender

    def execute(self):
        self.telebot_sender.send_doc(get_screenshot())


class CentralManager:
    def __init__(self, chat_id, token):
        token = '1453574410:AAE3xk-8w5PZZALLKoTcaL1qrGxiPUEQEcM'
        telebot_sender = TelebotSender(token, chat_id)

        self.commands = [
            SendScreenCommand(1, 1, telebot_sender),
            SendTextCommand(1, 2, '1', telebot_sender),
            SendTextCommand(1, 3, '2', telebot_sender),
            SendTextCommand(1, 4, '3', telebot_sender),
            SendTextCommand(1, 5, '4', telebot_sender),
            SendTextCommand(1, 6, '5', telebot_sender),
            SendTextCommand(1, 7, '6', telebot_sender),
            SendTextCommand(1, 12, 'Хочу', telebot_sender),
            SendTextCommand(1, 13, 'Решаю', telebot_sender),
            SendTextCommand(1, 14, 'Уноси', telebot_sender),
            SendTextCommand(2, 2, 'Да', telebot_sender),
            SendTextCommand(2, 3, 'Нет', telebot_sender),
        ]
        self.command_index = 0
        self.keyboard_grid = ChromaGrid('Keyboard')
        self.show_signs = True
        self.chroma_app = get_chroma_app()
        self.blink()

    def switch_command_up(self):
        self.command_index += 1

        if self.command_index >= len(self.commands):
            self.command_index = 0

        self.update_light()

    def execute_command(self):
        self.commands[self.command_index].execute()
        self.blink()

    def update_light(self):
        if not self.show_signs:
            self.chroma_app.Keyboard.setStatic(Colors.YELLOW)
        else:
            command = self.commands[self.command_index]
            self.keyboard_grid.set(hexcolor="#FFFF00")
            self.keyboard_grid[command.x][command.y].set(red=0, green=255, blue=0)
            self.chroma_app.Keyboard.setCustomGrid(self.keyboard_grid)
            self.chroma_app.Keyboard.applyGrid()

    def blink(self):
        self.chroma_app.Keyboard.setNone()
        sleep(0.3)
        self.chroma_app.Keyboard.setStatic(Colors.YELLOW)
        sleep(0.3)
        self.chroma_app.Keyboard.setNone()
        sleep(0.3)
        self.chroma_app.Keyboard.setStatic(Colors.YELLOW)
        self.update_light()


def get_chroma_app():
    info = ChromaAppInfo()
    info.DeveloperName = 'Rick Sanchez'
    info.DeveloperContact = 'Wubba-lubba@dub-dub.com'
    info.Category = 'application'
    info.SupportedDevices = ['keyboard']
    info.Description = 'Oh Rick, I don\'t know if that\'s a good idea.'
    info.Title = 'Mr Meeseeks Box'
    app = ChromaApp(info)
    return app


def get_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    photo = open('screenshot.png', 'rb')
    return photo
