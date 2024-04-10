import telebot, keyboard_bot, GAME
from random import randint
from telebot import types
from Bot_idetification import load_config
from Additional_Resources.lexicon import LEXICON_RU
from card_code.DECK import Deck
from card_code.PLAYER import Player
from card_code.BOT_ACTIONS import Bot_Game
#----------------------------------------------------------------
config = load_config()
bot = telebot.TeleBot(config.tg_bot.token)
deck = Deck()
Bot_Game = Bot_Game()
Player = Player()
game = GAME.Game()
#----------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, LEXICON_RU['/start'], reply_markup=keyboard_bot.first_keyboard())
    bot.register_next_step_handler(message, on_click_start)

def on_click_start(message):
    if message.text == LEXICON_RU['yes_button']:
        bot.send_message(message.chat.id, LEXICON_RU['start_game'])
        bot.send_message(message.chat.id, 'Окей', reply_markup=types.ReplyKeyboardRemove()) #Вмнесто окей поставить смайлы мастей (периодично меняющихся)
        bot.send_message(message.chat.id, 'Происходит перетасовка карт...'
                                          'Сейчас вы увидете свои карты', Game_Start(message), reply_markup=keyboard_bot.Player_field(Player.User_deck))
        rand = randint(0, 1)
        if rand == 0: #Переделать для дальнейших игр
            bot.send_photo(message.chat.id, Bot_Game.Atack_Bot(deck.Return_Trump()))
            bot.send_message(message.chat.id, LEXICON_RU['step_bot'])
            deck.first_step(rand)
            game.change_status()
        else:
            bot.send_message(message.chat.id, LEXICON_RU['step_yourself'])
            deck.first_step(rand)
            game.change_status()
    elif message.text == LEXICON_RU['no_button']:
        bot.send_message(message.chat.id, 'Зачем вы тогда открыли игру...')
        bot.send_message(message.chat.id, 'Окей', reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, LEXICON_RU['not_cmd'])

def Game_Start(message):
    deck.shuffle()
    bot.send_message(message.chat.id, f'{deck.GetDeck()} - козырь!')
    Bot_Game.GiveCards(deck.GiveAway_Card(Bot_Game.need_cards))
    Player.GiveCards(deck.GiveAway_Card(Player.need_cards))
    deck.field_add(message.text)
#bot.set_my_commands() -> after truble
@bot.message_handler(commands=['help'])
def help(message):
     bot.send_message(message.chat.id, LEXICON_RU['/help'])

@bot.message_handler(commands=['broken'])
def broken(message):
    bot.send_message(message.chat.id, LEXICON_RU['/broken'])

@bot.message_handler(commands=['take'])
def photo(message):
    bot.send_message(message.chat.id, LEXICON_RU['/take'])

@bot.message_handler(func=lambda mes: mes.text in Player.comparative_deck)
def condition_bot(message):
    if game.filter == True:
        deck.field_add(message.text)
        Player.Player_Attack(message.text)
        Bot_Game.protection_bot(message.text, deck)
        bot.send_message(message.chat.id, 'все было обработано')
@bot.message_handler(content_types=['text'])
def other_text(message):
    bot.send_message(message.chat.id, LEXICON_RU['not_cmd'])


bot.infinity_polling()


