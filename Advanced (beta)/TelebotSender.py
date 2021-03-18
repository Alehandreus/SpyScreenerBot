import telebot


class TelebotSender:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = telebot.AsyncTeleBot(token)

    def send_text(self, text):
        self.bot.send_message(self.chat_id, text)

    def send_doc(self, doc):
        self.bot.send_document(self.chat_id, doc)
