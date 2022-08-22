import telebot
from config import TOKEN, RU, EN

from gtts import gTTS
from loguru import logger
from os import remove

from DBcm import *


bot = telebot.TeleBot(TOKEN)

logger.add('./logs/applog.log', level='DEBUG')
logger.info('Start bot')

db = SQLighter('DB.db')
db.create_table()

try:
    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message):
        logger.info(f'[text] {message.chat.username} : {message.text}')
        bot.send_message(message.chat.id, text='/ru - russian voice,\n/en - english voice')

        if not db.user_exists(message.chat.id):
            db.add_user(message.chat.id, message.chat.username)

    @bot.message_handler(commands=['ru'])
    def handle_switching_to_russian(message):
        db.switch_lang(message.chat.id, RU)
        bot.send_message(message.chat.id, text='Switched on RU')
        logger.info(f'[switched on RU] : {message.chat.username}')

    @bot.message_handler(commands=['en'])
    def handle_switching_to_english(message):
        db.switch_lang(message.chat.id, EN)
        bot.send_message(message.chat.id, text='Switched on EN')
        logger.info(f'[switched on EN] : {message.chat.username}')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        logger.info(f'[text] {message.chat.username} : {message.text}')
        logger.debug(db.get_lang(message.chat.id))
        text = message.text
        if db.get_lang(message.chat.id) == RU:
            obj = gTTS(text, lang='ru')
        else:
            obj = gTTS(text, lang='en')
        obj.save('/tmp/voice.ogg')

        with open('/tmp/voice.ogg', 'rb') as voice:
            bot.send_voice(message.chat.id, voice)
        remove('/tmp/voice.ogg')


    bot.infinity_polling()

except Exception as error:
    db.close()
    logger.error(error)


logger.info('Stop bot')


