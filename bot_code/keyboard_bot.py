from telebot import types
from Additional_Resources.lexicon import LEXICON_RU
def first_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup_yes = types.KeyboardButton(LEXICON_RU['yes_button'])
    markup_no = types.KeyboardButton(LEXICON_RU['no_button'])
    markup.row(markup_yes, markup_no)
    return markup