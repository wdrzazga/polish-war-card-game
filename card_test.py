import unittest

from card import Card
from card_set import CardSet


class AllTests(unittest.TestCase):
    def test_card_get_value(self):
        ace_of_spades = Card(14, 'spades')
        self.assertEqual(ace_of_spades.get_value(), 'A')

    def test_card_set_creation(self):
        cs = CardSet()

        for card in cs.cards:
            print(card.to_string())

        self.assertEqual(len(cs.cards), 55)

if __name__ == '__main__':
    unittest.main()
