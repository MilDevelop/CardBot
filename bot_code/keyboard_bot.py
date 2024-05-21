from telebot import types
from Additional_Resources.lexicon import LEXICON_RU
from Additional_Resources.Ieraration import Hierarchy
from bot_code.GAME import Game

def start_keyboard():
    markup = types.ReplyKeyboardMarkup()
    card_game = types.KeyboardButton("Карты - Дурак")
    voice_inside = types.KeyboardButton("Voice inside")
    markup.row(card_game, voice_inside)
    return markup
def first_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup_yes = types.KeyboardButton(LEXICON_RU['yes_button'])
    markup_no = types.KeyboardButton(LEXICON_RU['no_button'])
    markup.row(markup_yes, markup_no)
    return markup

def Player_field(mass_card: list, game: Game):
    if len(mass_card) >= 1 and game.complete[0] == False:
        sorted_keys: list = []
        sorted_mass_card: dict = {}
        for el in mass_card:
            sorted_mass_card[el] = Hierarchy.index(el[0:len(el)-3])
        sorted_values = set(sorted(list(set(list(sorted_mass_card.values())))))
        print(sorted_values)
        for iter in sorted_values:
            for it in sorted_mass_card:
                if sorted_mass_card[it] == iter:
                    sorted_keys.append(it)
        markup = types.ReplyKeyboardMarkup()
        for i in range(len(sorted_keys)):
            mark = types.KeyboardButton(f"{sorted_keys[i][0:len(sorted_keys[i])-3]}-{sorted_keys[i][-2:]}") #фиксить твот тут примерно
            markup.row(mark)
        return markup
    else:
        markup = types.ReplyKeyboardRemove()
        return markup
