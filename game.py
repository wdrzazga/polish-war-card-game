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

    def turn(self):
        card1 = self.player1.active_deck.pop(0)
        card2 = self.player2.active_deck.pop(0)

        if card1.value > card2.value:
            self.player1.used_deck.append(card1)
            self.player1.used_deck.append(card2)
        elif card2.value > card1.value:
            self.player2.used_deck.append(card1)
            self.player2.used_deck.append(card2)
        else:
            stake = [card1, card2]
            while True:
                card1Hidden = self.player1.active_deck.pop(0)
                card2Hidden = self.player2.active_deck.pop(0)
                stake.append(card1Hidden)
                stake.append(card2Hidden)

                card1 = self.player1.active_deck.pop(0)
                card2 = self.player2.active_deck.pop(0)
                stake.append(card1)
                stake.append(card2)
                if card1.value != card2.value:
                    break

            if card1.value > card2.value:
                for card in stake:
                    self.player1.used_deck.append(card)

            elif card2.value > card1.value:
                for card in stake:
                    self.player2.used_deck.append(card)
