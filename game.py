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
        stake = [card1, card2]

        if card1.value > card2.value:
            self.player1.used_deck.extend(stake)
            print(f"{self.player1.name} wins the turn with {card1} against {card2}!")
        elif card2.value > card1.value:
            self.player2.used_deck.extend(stake)
            print(f"{self.player2.name} wins the turn with {card2} against {card1}!")
        else:
            print(f"It's a tie! Starting a war with {card1} and {card2}.")
            self.war(stake)

    def war(self, stake):
        while len(self.player1.active_deck) > 0 and len(self.player2.active_deck) > 0:
            if len(self.player1.active_deck) > 0:
                card1Hidden = self.player1.active_deck.pop(0)
                stake.append(card1Hidden)

            if len(self.player2.active_deck) > 0:
                card2Hidden = self.player2.active_deck.pop(0)
                stake.append(card2Hidden)

            if len(self.player1.active_deck) > 0 and len(self.player2.active_deck) > 0:
                card1 = self.player1.active_deck.pop(0)
                card2 = self.player2.active_deck.pop(0)
                stake.extend([card1, card2])

                if card1.value > card2.value:
                    self.player1.used_deck.extend(stake)
                    print(f"{self.player1.name} wins the war with {card1} against {card2}!")
                    return
                elif card2.value > card1.value:
                    self.player2.used_deck.extend(stake)
                    print(f"{self.player2.name} wins the war with {card2} against {card1}!")
                    return

            print("It's another tie during the war! Continuing...")
