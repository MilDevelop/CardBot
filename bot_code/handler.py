import telebot, keyboard_bot
from telebot import types
from Bot_idetification import load_config
from Additional_Resources.lexicon import LEXICON_RU
config = load_config()
bot = telebot.TeleBot(config.tg_bot.token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, LEXICON_RU['/start'], reply_markup=keyboard_bot.first_keyboard())
    bot.register_next_step_handler(message, on_click_start)
def on_click_start(message):
    if message.text == LEXICON_RU['yes_button']:
        bot.send_message(message.chat.id, LEXICON_RU['start_game'])
        bot.send_message(message.chat.id, 'Окей', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == LEXICON_RU['no_button']:
        bot.send_message(message.chat.id, 'Зачем вы тогда открыли игру...')
        bot.send_message(message.chat.id, 'Окей', reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, LEXICON_RU['not_cmd'])
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, LEXICON_RU['/help'])

@bot.message_handler(content_types=['text'])
def other_text(message):
    bot.send_message(message.chat.id, LEXICON_RU['not_cmd'])

bot.infinity_polling()