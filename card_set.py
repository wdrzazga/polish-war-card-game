from card import Card


class CardSet:
    def __init__(self):
        self.cards = []

        for value in range(2, 14+1):
            for symbol in ('spades', 'diamonds', 'hearts', 'clubs'):
                card = Card(value, symbol)
                self.cards.append(card)

        for color in ('black', 'red', 'blue'):
            joker = Card(15, color)
            self.cards.append(joker)
