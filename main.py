from random import randint
from datetime import date

class Card:
    number = None
    cvv = None
    card_date = None

    def __init__(self, cvv = None, number = None, card_date = None):
        self.set_data()

    def set_data(self, cvv = None, number = None, card_date = None):
        if number is None:
            self.numebr = self.generate_number()
        else:
            self.number = number

        if cvv is None:
            self.cvv = randint(100, 1000)

        if card_date is None:
            self.card_date = date.today().isoformat()

    def get_data(self):
        return f'Number: {self.number}\nCVV: {self.cvv}\nDate: {self.card_date}'

    def generate_number(self):
        self.number = ''
        self.number += str(randint(1000, 10000))

        for _ in range(3):
            n = randint(1000, 10000)

            while n == int(self.number[-1 * (len(self.number) - 2): -1]):
                n = randint(1000, 10000)

            self.number += str(n)

        return self.number


card = Card()