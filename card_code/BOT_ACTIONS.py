from Additional_Resources.Ieraration import Hierarchy
from Additional_Resources import lexicon
from card_code.DECK import Deck
class Bot_Game:
    def __init__(self):
        self.Bot_deck: list = []
        self.comparative_deck: list = []
        self.need_cards = 6 - len(self.Bot_deck)
    def GiveCards(self, main_deck: list):
        self.need_cards = 6 - len(self.Bot_deck)
        if self.need_cards <= 0:
            pass
        else:
            print(f"Нужно каарт боту----{self.need_cards}")
            for i in range(self.need_cards):
                self.Bot_deck.append(main_deck[i])
                self.comparative_deck.append(f"{main_deck[i]['value']}-{lexicon.simbol(main_deck[i]['suit'])}")

    def check_similar(self, card: str, deck: Deck):
        if len(deck.field) > 1:
            for iter in deck.field:
                if card[0:(len(card) - 3)] == iter[0:(len(iter) - 3)]:
                    return True
            return False
        return True

    def Atack_Bot(self, trump: str, deck: Deck):
        rang_card: dict = {}
        for element in self.Bot_deck:
            if element['suit'] != trump:
                if element['value'] in Hierarchy and self.check_similar(f"{element['value']}-{lexicon.simbol(element['suit'])}", deck):
                    rang_card[Hierarchy.index(element['value'])] = element
            elif element['suit'] == trump:
                if element['value'] in Hierarchy and self.check_similar(f"{element['value']}-{lexicon.simbol(element['suit'])}", deck):
                    rang_card[Hierarchy.index(element['value'])] = element
        if len(list(rang_card.keys())) != 0:
            index = self.Bot_deck.index(rang_card[min(list(rang_card.keys()))])
            deck.field_add(f"{self.Bot_deck[index]['value']}-{lexicon.simbol(self.Bot_deck[index]['suit'])}")
            self.Bot_deck.remove(rang_card[min(list(rang_card.keys()))])
            self.comparative_deck.pop(self.comparative_deck.index(self.comparative_deck[index]))
            return [True, rang_card[min(list(rang_card.keys()))]['image']]
        else:
            return [False]

    def protection_bot(self, attack_card, deck: Deck) -> list:
        attack_status = attack_card[0:len(attack_card)-3]
        attack_mast = attack_card[-2:]
        maybe: list = []
        trump_maybe: list = []
        for iter in self.comparative_deck: #?
            if iter[-2:] == lexicon.simbol(deck.Return_Trump()):
                trump_maybe.append(iter)
            elif iter[-2:] == attack_mast:
                maybe.append(iter)
        if len(trump_maybe) != 0:
            test_mass: dict = {} #индексы козырных элементов в иерархии
            for el in trump_maybe:
                test_mass[Hierarchy.index(el[0:len(el)-3])] = el
            if len(list(test_mass.keys())) != 0:
                ix = test_mass[min(list(test_mass.keys()))]
                photo = None
                for elem in self.Bot_deck:
                    if elem == self.Bot_deck[self.comparative_deck.index(ix)]:
                        photo = elem['image']
                deck.field_add(f"{self.Bot_deck[self.comparative_deck.index(ix)]['value']}-{lexicon.simbol(self.Bot_deck[self.comparative_deck.index(ix)]['suit'])}")
                self.Bot_deck.pop(self.comparative_deck.index(ix))
                self.comparative_deck.pop(self.comparative_deck.index(ix))
                trump_maybe.pop(trump_maybe.index(ix))
                return [True, photo]
            else:
                return [False]

        else:
            test_mass: dict = {}
            for el in maybe:
                if Hierarchy.index(el[0:len(el)-3]) > Hierarchy.index(attack_status):
                    test_mass[Hierarchy.index(el[0:len(el)-3])] = el
            if len(list(test_mass.keys())) != 0:
                ix = test_mass[min(list(test_mass.keys()))]
                photo = None
                for elem in self.Bot_deck:
                    if elem == self.Bot_deck[self.comparative_deck.index(ix)]:
                        photo = elem['image']
                deck.field_add(f"{self.Bot_deck[self.comparative_deck.index(ix)]['value']}-{lexicon.simbol(self.Bot_deck[self.comparative_deck.index(ix)]['suit'])}")
                self.Bot_deck.pop(self.comparative_deck.index(ix))
                self.comparative_deck.pop(self.comparative_deck.index(ix))
                maybe.pop(maybe.index(ix))
                return [True, photo]
            else:
                return [False]
    def bot_take(self, deck: Deck) -> None:
        for item in deck.field:
            dictionary: dict = {}
            dictionary['value'] = item[0:len(item)-3]
            dictionary['suit'] = item[-2:]
            dictionary['image'] = deck.images[item]
            self.Bot_deck.append(dictionary)
            self.comparative_deck.append(item)
