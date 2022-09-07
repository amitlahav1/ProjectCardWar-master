from random import randint
import random

class DeckOfCards:
    def __init__(self,):
#cards deck 52
        self.deck52 = []
        for s in "Diamond", "Spade", "Heart", "Club":
            for v in range(1, 14, 1):
                self.deck52.append((s, v))
    def __str__(self):
        return f"main deck : {self.deck52}"
    def ace_power(self):
        for card in self.deck52:
            if card.value == 1:
                card.value = 14

    def cards_shuffle(self):
        random.shuffle(self.deck52)

    def del_one(self):
        return self.deck52.pop(randint(0, len(self.deck52)-1))





