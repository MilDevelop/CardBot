import telebot
from dataclasses import dataclass
from environs import Env
import telebot
@dataclass
class TgBot:
    token: str

def load_token(path: str | None = None) -> TgBot:
    env = Env()
    env.read_env(path)
    return TgBot(token=env('BOT_TOKEN'))

bot = telebot.TeleBot(load_token().token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "...")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "help")