class Card:
    def __init__(self, value: int, symbol: str):
        self.value = value
        self.symbol = symbol

        if 2 > self.value > 15:
            raise Exception("Wrong value. Input a value from 2 to 15")

    def get_value(self):
        if 1 < self.value < 11:
            return str(self.value)
        elif self.value == 11:
            return 'J'
        elif self.value == 12:
            return 'Q'
        elif self.value == 13:
            return 'K'
        elif self.value == 14:
            return 'A'
        else:
            return 'Joker'

    def to_string(self):
        return str(self.get_value() + ' ' + self.symbol)
