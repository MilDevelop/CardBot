import telebot
import keyboard_bot
import GAME
from random import randint
from telebot import types
from Bot_idetification import load_config
from Additional_Resources.lexicon import LEXICON_RU, simbol
from card_code.DECK import Deck
from card_code.PLAYER import Player
from card_code.BOT_ACTIONS import Bot_Game
# ----------------------------------------------------------------
config = load_config()
bot = telebot.TeleBot(config.tg_bot.token)
deck = Deck()
Bot_Game = Bot_Game()
Player = Player()
game = GAME.Game()
bot_attack = [False, False]
# ----------------------------------------------------------------


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Во что будете играть?", reply_markup=keyboard_bot.start_keyboard())
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Карты - Дурак":
        bot.send_message(message.chat.id, LEXICON_RU['/start'], reply_markup=keyboard_bot.first_keyboard())
        bot.register_next_step_handler(message, on_click_start_card)
    elif message.text == "Voice inside":
        pass
def on_click_start_card(message):
    if message.text == LEXICON_RU['yes_button']:
        bot.send_message(message.chat.id, LEXICON_RU['start_game'])
        bot.send_message(message.chat.id, 'Окей', reply_markup=types.ReplyKeyboardRemove())  # Вместо 'окей' ->
        # поставить смайлы мастей (периодично меняющихся)
        bot.send_message(message.chat.id, 'Происходит перетасовка карт...'
                                          'Сейчас вы увидете свои карты', Game_Start(message), reply_markup=keyboard_bot
                         .Player_field(Player.comparative_deck, game))
        rand = randint(0, 1)
        game.filter = False
        game.add_player(message.chat.id, message.chat.first_name)
        if rand == 0:  # Переделать для дальнейших игр
            bot.send_photo(message.chat.id, Bot_Game.Atack_Bot(deck.Return_Trump(), deck)[1])
            bot.send_message(message.chat.id, LEXICON_RU['step_bot'])
            deck.first_step(rand)
            game.filter = True
        else:
            bot.send_message(message.chat.id, LEXICON_RU['step_yourself'])
            deck.first_step(rand)
            game.filter = False
    elif message.text == LEXICON_RU['no_button']:
        bot.send_message(message.chat.id, 'Зачем вы тогда открыли игру...')
        bot.send_message(message.chat.id, 'Окей', reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, LEXICON_RU['not_cmd'])


def Game_Start(message):
    deck.shuffle()
    to_pin = bot.send_message(message.chat.id, f'{simbol(deck.GetDeck())} - козырь!').message_id
    bot.pin_chat_message(message.chat.id, message_id=to_pin)
    Runtime_Check_finish()
    Bot_Game.GiveCards(deck.GiveAway_Card(Bot_Game.NEED_CARDS()))
    Player.GiveCards(deck.GiveAway_Card(Player.NEED_CARDS()))


def complete(message):
    keyboard_bot.Player_field(Player.comparative_deck, game)
    if game.complete[1] == "Player":
        bot.send_message(message.chat.id, LEXICON_RU['win'], reply_markup=keyboard_bot.Player_field([0], game))
        game.filter = None
        game.add_score()
    if game.complete[1] == "Bot":
        bot.send_message(message.chat.id, LEXICON_RU['lose'], reply_markup=keyboard_bot.Player_field([0], game))
        game.filter = None


def Runtime_Check_finish() -> bool:
    if len(deck.main_deck) > 12 - (len(Player.User_deck) + len(Bot_Game.Bot_deck)):
        deck.full_take = True
        return True
    elif len(deck.main_deck) == 0:
        deck.full_take = False
        print("ERROR")
        if len(Player.User_deck) == 0:
            game.complete = [True, "Player"]
            return False
        if len(Bot_Game.Bot_deck) == 0:
            game.complete = [True, "Bot"]
            return False
        return True
    elif len(deck.main_deck) <= 12 - (len(Player.User_deck) + len(Bot_Game.Bot_deck)):  # Вот тут можно вмепсто < 0 поставить 1
        deck.full_take = None
        if len(Player.User_deck) - len(Bot_Game.Bot_deck) > 0:
            deck.diff = abs(len(Player.User_deck) - len(Bot_Game.Bot_deck))  # Если true -> у игрока больше карт
        else:
            deck.diff = abs(len(Player.User_deck) - len(Bot_Game.Bot_deck))
        return True


def bot_brokenCMD_actions(message):
    bot.send_message(message.chat.id, LEXICON_RU['step_bot'])
    bot_attack = Bot_Game.Atack_Bot(deck.Return_Trump(), deck)
    if bot_attack[0] is True:
        bot.send_photo(message.chat.id, bot_attack[1], reply_markup=keyboard_bot.Player_field(Player.
                                                                                              comparative_deck, game))
    else:
        bot.send_message(message.chat.id, "Нечего подктдывать, Бито!")
        game.filter = False
        deck.garbage_deck = deck.field.copy()
        deck.field.clear()
        if Runtime_Check_finish():
            Bot_Game.GiveCards(deck.GiveAway_Card(Bot_Game.NEED_CARDS()))
        if Runtime_Check_finish():
            Player.GiveCards(deck.GiveAway_Card(Player.NEED_CARDS()))
        bot.send_message(message.chat.id, "Получите свои карты",
                         reply_markup=keyboard_bot.Player_field(Player.comparative_deck, game))


def bot_takeCMD_actions(message):
    bot.send_message(message.chat.id, "Игра разворачивается с новой силой!",
                     reply_markup=keyboard_bot.Player_field(Player.comparative_deck, game))
    bot.send_message(message.chat.id, LEXICON_RU['step_bot'])
    bot_attack = Bot_Game.Atack_Bot(deck.Return_Trump(), deck)
    if bot_attack[0] is True:  # maybe
        bot.send_photo(message.chat.id, bot_attack[1])
    game.filter = True

# ------------------------------------------------------------------------------------------------
# bot.set_my_commands() -> after truble


@bot.message_handler(commands=['help'])
def help(message):
     bot.send_message(message.chat.id, LEXICON_RU['/help'])


@bot.message_handler(commands=['stat'])
def stat(message):
    bot.send_message(message.chat.id, f"Ваш счёт - {game.score}")


@bot.message_handler(commands=['broken'])
def broken(message):
    bot.send_message(message.chat.id, LEXICON_RU['/broken'])
    deck.garbage_deck = deck.field.copy()
    deck.field.clear()
    if Runtime_Check_finish():
        Bot_Game.GiveCards(deck.GiveAway_Card(Bot_Game.NEED_CARDS()))
    if Runtime_Check_finish():
        Player.GiveCards(deck.GiveAway_Card(Player.NEED_CARDS()))
        game.filter = True
        bot_brokenCMD_actions(message)
    else:
        complete(message)


@bot.message_handler(commands=['take'])
def take(message):
    bot.send_message(message.chat.id, LEXICON_RU['/take'])
    Player.player_take(deck)
    deck.field.clear()
    if Runtime_Check_finish():
        Bot_Game.GiveCards(deck.GiveAway_Card(Bot_Game.NEED_CARDS()))
        bot_takeCMD_actions(message)
    else:
        complete(message)


@bot.message_handler(func=lambda mes: mes.text in Player.comparative_deck and game.filter is False and game.
                     complete[0] is False)
def condition_bot_protection(message):
    if deck.check_similar(message.text) or len(deck.field) <= 1:
        Player.Player_field(message.text, deck)
        card_photo = Bot_Game.protection_bot(message.text, deck)
        if card_photo[0] is True:
            bot.send_photo(message.chat.id, card_photo[1], reply_markup=keyboard_bot.
                           Player_field(Player.comparative_deck, game))
            print(f"field{deck.field}")
        else:
            bot.send_message(message.chat.id, "У меня нечем биться, беру")
            Bot_Game.bot_take(deck)
            deck.field.clear()
            if Runtime_Check_finish():
                Player.GiveCards(deck.GiveAway_Card(Player.NEED_CARDS()))
                bot.send_message(message.chat.id, "Получите свои карты из колоды", reply_markup=keyboard_bot.
                                 Player_field(Player.comparative_deck, game))
                bot.send_message(message.chat.id, LEXICON_RU['step_yourself'])
            else:
                complete(message)
    else:
        bot.send_message(message.chat.id, "Шуллер!")


@bot.message_handler(func=lambda mes: mes.text in Player.comparative_deck and game.filter is True and game.
                     complete[0] is False)
def condition_bot_attack(message):
    Player.Player_field(message.text, deck)  # Пока полагаемся на разумность игрока
    bot_attack = Bot_Game.Atack_Bot(deck.Return_Trump(), deck)
    if bot_attack[0] is True:
        bot.send_photo(message.chat.id, bot_attack[1], reply_markup=keyboard_bot.Player_field(Player.
                                                                                              comparative_deck, game))
    else:
        bot.send_message(message.chat.id, "Нечего подктдывать, Бито!")
        game.filter = False
        deck.garbage_deck = deck.field.copy()
        deck.field.clear()
        if Runtime_Check_finish():
            Bot_Game.GiveCards(deck.GiveAway_Card(Bot_Game.NEED_CARDS()))
        if Runtime_Check_finish():
            Player.GiveCards(deck.GiveAway_Card(Player.NEED_CARDS()))
            bot.send_message(message.chat.id, "Получите свои карты", reply_markup=keyboard_bot.
                             Player_field(Player.comparative_deck, game))
            bot.send_message(message.chat.id, LEXICON_RU['step_yourself'])
        else:
            complete(message)


@bot.message_handler(content_types=['text'])
def other_text(message):
    bot.send_message(message.chat.id, LEXICON_RU['not_cmd'])


bot.infinity_polling()
