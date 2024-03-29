class Player:
    def __init__(self):
        self.User_deck: list = []
        self.need_cards = 6 - len(self.User_deck)
    def GiveCards(self, main_deck: list):
        if self.need_cards <= 0:
            pass
        else:
            for i in range(self.need_cards):
                self.User_deck.append(main_deck[i])