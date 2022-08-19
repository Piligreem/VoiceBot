import telebot
from config import TOKEN

from gtts import gTTS


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, text='Hello!')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    obj = gTTS(text, lang='ru')
    obj.save('/tmp/voice.ogg')
    voice = open('/tmp/voice.ogg', 'rb')

    bot.send_voice(message.chat.id, voice)


bot.infinity_polling()

