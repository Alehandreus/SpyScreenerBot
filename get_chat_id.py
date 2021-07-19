import telebot


token = input("Bot Token:\n")
bot = telebot.AsyncTeleBot(token)
print()
print("Send any message to your bot")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.chat.id)
    print("Chat id:", message.chat.id)


bot.polling()
