from telebot import types
from Additional_Resources.lexicon import LEXICON_RU
from bot_code.GAME import Game


def first_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup_yes = types.KeyboardButton(LEXICON_RU['yes_button'])
    markup_no = types.KeyboardButton(LEXICON_RU['no_button'])
    markup.row(markup_yes, markup_no)
    return markup


def Player_field(mass_card: list, game: Game):
    if len(mass_card) >= 1 and game.filter is not None:
        markup = types.ReplyKeyboardMarkup()
        for i in range(len(mass_card)):
            mark = types.KeyboardButton(f"{mass_card[i][0:len(mass_card[i])-3]}-{mass_card[i][-2:]}")  # Фиксить твот ->
            # тут примерно
            markup.row(mark)
        return markup
    else:
        markup = types.ReplyKeyboardRemove()
        return markup
