import telebot


token = input("Токен бота:\n")
bot = telebot.AsyncTeleBot(token)
print()
print("Напишите боту в любом чате, он пришлет в ответ id чата")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.chat.id)


bot.polling()
