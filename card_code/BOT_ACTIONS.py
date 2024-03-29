from Additional_Resources.Ieraration import Hierarchy
class Bot_Game:
    def __init__(self):
        self.Bot_deck: list = []
        self.need_cards = 6 - len(self.Bot_deck)

    def GiveCards(self, main_deck: list):
        if self.need_cards <= 0:
            pass
        else:
            for i in range(self.need_cards):
                self.Bot_deck.append(main_deck[i])

    def Atack_Bot(self):
        rang_card: dict = {}
        for element in self.Bot_deck:
            if element in Hierarchy:
                print(Hierarchy.index(element))
                rang_card[Hierarchy.index(element)] = element
        self.Bot_deck.pop(rang_card[min(list(rang_card.keys()))])
        return rang_card[min(list(rang_card.keys()))]['images']['png']

