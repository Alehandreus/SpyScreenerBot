# SpyScreenerBot

Сперва необходимо создать бота при помощи BotFather в Telegram

## Classic

Висит в фоне и по комбинациям клавиш отправляет скриншот или текстовое сообщение в диалог в Telegram

- файл main_classic.pyw:
    - в IDE запускается, как и файл .py
    - при запуске вне IDE скрипт не открывает консоль и выполняется в фоне. Закрыть его можно через диспетчер задач (процесс python) или комбинацией клавиш
- файл settings.py:
    - token: токен telegram бота
    - chat_id: id чата, в который отправлять сообщения.  
**Узнать id чата можно с помощью get_chat_id.py**
    - send_screenshot_hotkeys: список комбинаций клавиш, по которым отправляется скриншот (комбинация может состоять из одной клавиши).  
**Узнать названия клавиш можно с помощью get_key_name.py**
    - stop_hotkeys: комбинации, по которым программа завершается
    - send_text_hotkeys: комбинации, которые отправляют текстовые сообщения

- библиотеки:
    - pynput (отслеживание нажатых клавиш)
    - pyautogui (скриншот)
    - telebot (pyTelegramBotAPI) (telegram бот)
