import telebot
from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

def load_token(path: str = None) -> TgBot:
    env = Env()
    env.read_env(path)
    return TgBot(token=env('BOT_TOKEN'))