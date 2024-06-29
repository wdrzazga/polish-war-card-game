import unittest

from card import Card
from card_set import CardSet
from game import Game


class AllTests(unittest.TestCase):
    def test_card_get_value(self):
        ace_of_spades = Card(14, 'spades')
        self.assertEqual(ace_of_spades.get_value(), 'A')

    def test_card_set_creation(self):
        cs = CardSet()

        for card in cs.cards:
            print(card.to_string())

        self.assertEqual(len(cs.cards), 4 * 13 + 3)

    def test_card_set_shuffle(self):
        cs = CardSet()
        cs.shuffle()

        for card in cs.cards:
            print(card.to_string())

        self.assertEqual(len(cs.cards), 4 * 13 + 3)

    def test_game_card_distribution(self):
        g = Game()

        for i, card in enumerate(g.player1.active_deck):
            print(str(i + 1) + '   ' + card.to_string())

        print('------------------')

        for i, card in enumerate(g.player2.active_deck):
            print(str(i + 1) + '   ' + card.to_string())



if __name__ == '__main__':
    unittest.main()
