class Bot_Game:
    def __init__(self):
        self.Bot_deck: list = []
    def GiveCards(self, main_deck: list) -> tuple:
        counter_card = 6 - len(self.Bot_deck)
        if counter_card >= 6:
            pass
        else:
            for i in range(counter_card):
                self.Bot_deck.append(main_deck[i])
                main_deck.remove(main_deck[i])
        return (self.Bot_deck, main_deck)

