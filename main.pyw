import logging
import os
from aiogram import Bot, Dispatcher, executor, types
import pyautogui


API_TOKEN = '1453574410:AAE3xk-8w5PZZALLKoTcaL1qrGxiPUEQEcM'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['s'])
async def screen(message: types.Message):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        photo = open('screenshot.png', 'rb')
        # await message.answer_photo(photo)
        await message.answer_document(photo)
        os.remove('screenshot.png')
    except Exception as e:
        print(e)
        await message.answer('Возникла ошибка')


@dp.message_handler(commands=['s2'])
async def screen2(message: types.Message):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        photo = open('screenshot.png', 'rb')
        await message.answer_photo(photo)
        os.remove('screenshot.png')
    except Exception as e:
        print(e)
        await message.answer('Возникла ошибка')

executor.start_polling(dp)
