from Card_Class import Card
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

    def cards_shuffle(self):
        random.shuffle(self.deck52)

    def del_one(self):
        return self.deck52.pop(randint(0, len(self.deck52)-1))





# d = DeckOfCards()
# d.cards_shuffle()
# print(d.deck52)
# print(d.del_one())
#
# print(d.deck52)