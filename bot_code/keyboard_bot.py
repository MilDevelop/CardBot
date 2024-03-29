from telebot import types
from Additional_Resources.lexicon import LEXICON_RU, simbol
def first_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup_yes = types.KeyboardButton(LEXICON_RU['yes_button'])
    markup_no = types.KeyboardButton(LEXICON_RU['no_button'])
    markup.row(markup_yes, markup_no)
    return markup

def Player_field(mass_card: list):
    markup = types.ReplyKeyboardMarkup()
    for i in range(len(mass_card)):
        mark = types.KeyboardButton(f"{mass_card[i]['value']} - {simbol(mass_card[i]['suit'])}") #размерность карты пример: (9, валет, 10, король)
        markup.row(mark)
    return markup
