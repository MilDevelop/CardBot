#         Point = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1"
#         self.bot_card = requests.get(Point).json()
#         pprint.pprint(self.bot_card)
#         ImageRandCard = self.bot_card['cards'][0]['images']['png']
#         Mast = self.bot_card['cards'][0]['suit']
#         return (ImageRandCard, Mast[0])
#
#     def Check(self, user_mast: str, bot_mast: str):
#         return user_mast[-1] == bot_mast.lower()
import requests, pprint
from random import choice
class Deck:
    def __init__(self):
        self.deck_id: str
        self.main_deck: list
        self.garbage_deck: list
        self.field: list
        self.trump_card: str
        self.first_field: int
    def shuffle(self):
        endPoint = "https://deckofcardsapi.com/api/deck/new/shuffle/"
        params = {"deck_count": 1}
        response = requests.get(endPoint, params=params)
        self.deck_id= response.json()["deck_id"]
    def GetDeck(self):
        Point = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=52"
        self.main_deck = requests.get(Point).json()['cards']
        self.trump_card = choice(['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS'])
        return self.trump_card

    def first_step(self, number: int):
        self.first_field = number
    def Return_Trump(self) -> str:
        return self.trump_card
    def GiveAway_Card(self, need_cards) -> list:
        Given_Cards = []
        for item in range(need_cards):
            pprint.pprint(self.main_deck[item])
            Given_Cards.append(self.main_deck[item])
            self.main_deck.remove(self.main_deck[item])
        return Given_Cards


