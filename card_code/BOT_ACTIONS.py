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

