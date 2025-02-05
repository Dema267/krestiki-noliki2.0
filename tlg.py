import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
TOKEN = '8015633635:AAFUbuSQvDMvjcJClAqa5Fr-nnjmhJ2sBA8'
bot = telebot.TeleBot(TOKEN)

# Обработчик для приёма текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "этот бот лежит на локальном сервере")

# Запуск бота
bot.polling()