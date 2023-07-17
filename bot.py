import telebot

# Replace 'YOUR_API_TOKEN' with your actual API token
API_TOKEN = '6399381224:AAEF3QDoyOLn1ONBGsJZHRdeSs4v1kNTgOY'
bot = telebot.TeleBot(API_TOKEN)

# /start command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm your bot. How can I assist you?")

# Message handler to echo back any text messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_text(message):
    bot.send_message(message.chat.id, message.text)

# Message handler for voice messages
@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    bot.send_message(message.chat.id, "You sent a voice message!")

# Start the bot with long polling
bot.polling()
