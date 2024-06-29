
from card_set import CardSet
from player import Player


class Game:
    def __init__(self):
        self.player1 = Player('Alien')
        self.player2 = Player('Human')
        card_set = CardSet()
        card_set.shuffle()
        self.card_set = card_set

        while len(self.card_set.cards) > 0:
            c = self.card_set.cards.pop(0)
            self.player1.active_deck.append(c)

            if len(self.card_set.cards) > 0:
                c = self.card_set.cards.pop(0)
                self.player2.active_deck.append(c)

        print("Game started!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
