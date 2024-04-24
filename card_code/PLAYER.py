from Additional_Resources import lexicon, Ieraration
from card_code.DECK import Deck
class Player:
    def __init__(self):
        self.User_deck: list = []
        self.comparative_deck: list = []
        self.need_cards: int = 6 - len(self.User_deck)
    def GiveCards(self, main_deck: list):
        self.need_cards = 6 - len(self.User_deck)
        if self.need_cards <= 0:
            pass
        else:
            for i in range(self.need_cards):
                self.User_deck.append(main_deck[i])
                self.comparative_deck.append(f"{main_deck[i]['value']}-{lexicon.simbol(main_deck[i]['suit'])}")

    def check_field_player(self, given_card: str, field, deck: Deck) -> bool: #what is it???
        if field[-2:] == lexicon.simbol(deck.Return_Trump()):
            return True
        elif field[-2:] == given_card[-2:]:
            if Ieraration.Hierarchy.index(field[0:len(field) - 3]) > Ieraration.Hierarchy.index(given_card[0:len(field) - 3]):
                return True
            return False
        return False

    def Player_field(self, field, deck: Deck):
        deck.field_add(field)
        index = self.comparative_deck.index(field)
        self.comparative_deck.pop(index)
        self.User_deck.pop(index)

    def player_take(self, deck: Deck) -> None:
        print(deck.field)
        for item in deck.field:
            print(item)
            dictionary: dict = {}
            dictionary['value'] = item[0:len(item) - 3]
            dictionary['suit'] = lexicon.ober_simbol(item[-2:])
            dictionary['image'] = deck.images[item]
            self.User_deck.append(dictionary)
            self.comparative_deck.append(item)
    def NEED_CARDS(self) -> int:
        self.need_cards = 6 - len(self.User_deck)
        return self.need_cards