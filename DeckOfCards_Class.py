from random import randint
import random
from Card_Class import Card


class DeckOfCards:
    def __init__(self):
        # define deck of cards objects.
        self.deck52 = []
        for s in "Diamond", "Spade", "Heart", "Club":
            for v in range(1, 14, 1):
                self.deck52.append(Card(s, v))
        self.ace_power()

    def __str__(self):
        # print the object in class DeckOfCards.
        return f"main deck : {self.deck52}"

    def ace_power(self):
        # make sure that the ACE is the strongest card in the game.
        for card in self.deck52:
            if card.value == 1:
                card.value = 14

    def cards_shuffle(self):
        # shuffle that deck of cards.
        random.shuffle(self.deck52)

    def del_one(self):
        # delete a random card from the deck, (delete mean give to player ====> in later function).
        return self.deck52.pop(randint(0, len(self.deck52)-1))

