# class card_deck1:
#     def __init__(self):
#         self.deck_id: str
#     async def shuffle(self):
#         endPoint = "https://deckofcardsapi.com/api/deck/new/shuffle/"
#         params = {"deck_count": 1}
#         response = requests.get(endPoint, params=params)
#         self.deck_id= response.json()["deck_id"]
#     async def GetCard(self):
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
class Deck:
    def __init__(self):
         self.deck_id: str
    def shuffle(self):
        endPoint = "https://deckofcardsapi.com/api/deck/new/shuffle/"
        params = {"deck_count": 1}
        response = requests.get(endPoint, params=params)
        self.deck_id= response.json()["deck_id"]
    def GetDeck(self):
        Point = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=36"
        self.bot_card = requests.get(Point).json()

