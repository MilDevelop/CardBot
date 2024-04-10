from Additional_Resources import lexicon
class Player:
    def __init__(self):
        self.User_deck: list = []
        self.comparative_deck: list = []
        self.need_cards = 6 - len(self.User_deck)
    def GiveCards(self, main_deck: list):
        if self.need_cards <= 0:
            pass
        else:
            for i in range(self.need_cards):
                self.User_deck.append(main_deck[i])
                self.comparative_deck.append(f"{main_deck[i]['value']}-{lexicon.simbol(main_deck[i]['suit'])}")
    def Player_Attack(self, field):
        index = self.comparative_deck.index(field)
        self.comparative_deck.pop(index)
        self.User_deck.pop(index)

