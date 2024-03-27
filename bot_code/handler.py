import telebot
from Bot_idetification import load_token
from Additional_Resources.lexicon import LEXICON_RU
bot = telebot.TeleBot(load_token().token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, LEXICON_RU['/start'])

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, LEXICON_RU['/help'])

@bot.message_handler(content_types=['text'])
def other_text(message):
    bot.send_message(message.chat.id, LEXICON_RU['/other_text'])