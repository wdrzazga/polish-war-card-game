import unittest

from card import Card
from game import Game


class AllTests(unittest.TestCase):
    def test_war(self):
        game = Game()
        game.player1.active_deck.clear()
        game.player2.active_deck.clear()

        game.player1.active_deck.append(Card(3, 'spades'))
        game.player1.active_deck.append(Card(11, 'spades'))
        game.player1.active_deck.append(Card(7, 'hearts'))

        game.player2.active_deck.append(Card(3, 'hearts'))
        game.player2.active_deck.append(Card(14, 'spades'))
        game.player2.active_deck.append(Card(8, 'spades'))

        game.turn()

        self.assertEqual(len(game.player2.used_deck), 6)
        self.assertEqual(len(game.player1.used_deck), 0)

    def test_long_war(self):
        game = Game()
        game.player1.active_deck.clear()
        game.player2.active_deck.clear()

        game.player1.active_deck.append(Card(11, 'spades'))
        game.player1.active_deck.append(Card(8, 'spades'))
        game.player1.active_deck.append(Card(4, 'diamonds'))
        game.player1.active_deck.append(Card(9, 'hearts'))
        game.player1.active_deck.append(Card(4, 'hearts'))

        game.player2.active_deck.append(Card(11, 'hearts'))
        game.player2.active_deck.append(Card(6, 'spades'))
        game.player2.active_deck.append(Card(4, 'spades'))
        game.player2.active_deck.append(Card(10, 'diamonds'))
        game.player2.active_deck.append(Card(5, 'clubs'))

        game.turn()

        self.assertEqual(len(game.player2.used_deck), 10)
        self.assertEqual(len(game.player1.used_deck), 0)
