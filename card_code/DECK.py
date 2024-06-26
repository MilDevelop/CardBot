#         Point = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1"
#         self.bot_card = requests.get(Point).json()
#         pprint.pprint(self.bot_card)
#         ImageRandCard = self.bot_card['cards'][0]['images']['png']
#         Mast = self.bot_card['cards'][0]['suit']
#         return (ImageRandCard, Mast[0])
#
#     def Check(self, user_mast: str, bot_mast: str):
#         return user_mast[-1] == bot_mast.lower()
import requests, pprint  # BaCat: я не уверен, но это вроде 'pprint' не нужен
from random import choice
from Additional_Resources.lexicon import simbol


class Deck:
    def __init__(self):
        self.deck_id: str
        self.main_deck: list = []
        self.garbage_deck: list = []
        self.field: list = []
        self.trump_card: str
        self.first_field: int
        self.images: dict = {}
        self.diff: int = 0
        self.full_take = True

    def shuffle(self):
        endPoint = "https://deckofcardsapi.com/api/deck/new/shuffle/"
        params = {"deck_count": 1}
        response = requests.get(endPoint, params=params)
        self.deck_id = response.json()["deck_id"]

    def GetDeck(self):
        Point = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=52"
        self.main_deck = requests.get(Point).json()['cards']
        self.trump_card = choice(['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS'])
        for item in self.main_deck:
            self.images[f"{item['value']}-{simbol(item['suit'])}"] = item['image']
        return self.trump_card

    def first_step(self, number: int):
        self.first_field = number

    def Return_Trump(self):
        return self.trump_card

    def Return_Diff(self):
        return self.diff

    def GiveAway_Card(self, need_cards):  # obj -> кому отдаем
        print(f"{len(self.main_deck)}")
        if self.full_take is True:
            if need_cards >= 1:
                Given_Cards = []
                for item in range(need_cards):
                    Given_Cards.append(self.main_deck[item])
                    self.main_deck.remove(self.main_deck[item])
                return Given_Cards
            else:
                pass
        elif self.full_take is None:
            print("Im Here")
            Given_Cards = []
            for item in self.main_deck:
                Given_Cards.append(item)
                self.main_deck.remove(item)
            self.full_take = False
            return Given_Cards
        else:
            pass

    def field_add(self, card: str):
        self.field.append(card)

    def check_similar(self, card: str):
        for iter in self.field:
            if card[0:(len(card) - 3)] == iter[0:(len(iter) - 3)]:
                return True
        return False
