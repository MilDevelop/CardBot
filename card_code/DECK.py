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
import PLAYER, BOT_ACTIONS
class Deck:
    def __init__(self):
        self.deck_id: str
        self.main_deck: list
        self.garbage_deck: list
        self.field: list
    def shuffle(self):
        endPoint = "https://deckofcardsapi.com/api/deck/new/shuffle/"
        params = {"deck_count": 1}
        response = requests.get(endPoint, params=params)
        self.deck_id= response.json()["deck_id"]
    def GetDeck(self):
        Point = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=36"
        self.main_deck = requests.get(Point).json()['cards']
        return self.main_deck
    def GiveAway_Card(self):
        self.main_deck.remove('')


