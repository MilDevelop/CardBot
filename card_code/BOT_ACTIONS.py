from Additional_Resources.Ieraration import Hierarchy
from Additional_Resources import lexicon
from DECK import Deck
class Bot_Game:
    def __init__(self):
        self.Bot_deck: list = []
        self.comparative_deck: list = []
        self.need_cards = 6 - len(self.Bot_deck)
    def GiveCards(self, main_deck: list):
        if self.need_cards <= 0:
            pass
        else:
            for i in range(self.need_cards):
                self.Bot_deck.append(main_deck[i])
                self.comparative_deck.append(f"{main_deck[i]['value']}-{lexicon.simbol(main_deck[i]['suit'])}")

    def Atack_Bot(self, trump: str):
        rang_card: dict = {}
        for element in self.Bot_deck:
            if element['suit'] != trump:
                if element['value'] in Hierarchy:
                    rang_card[Hierarchy.index(element['value'])] = element
        index = self.Bot_deck.index(rang_card[min(list(rang_card.keys()))])
        self.Bot_deck.remove(rang_card[min(list(rang_card.keys()))])
        self.comparative_deck.pop(self.comparative_deck[index])
        return rang_card[min(list(rang_card.keys()))]['images']['png']
    def protection_bot(self, attack_card, deck: Deck):
        attack_status = attack_card[0:len(attack_card)-3]
        attack_mast = attack_card[-1]
        maybe: list = []
        for iter in self.comparative_deck:
            if iter[-1] == lexicon.simbol(deck.Return_Trump()) or iter[-1] == attack_mast:
                maybe.append(iter)

