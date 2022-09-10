from Card_Class import Card
from random import randint
from DeckOfCards_Class import DeckOfCards



class Player:
    def __init__(self, name, player_cards_amount=26):
        # define player object in Player class.
        if name == "":  # (name)
            name = "player1"
        if type(player_cards_amount) != int:
            player_cards_amount = 26
        if 10 > player_cards_amount or player_cards_amount > 26:
            player_cards_amount = 26

        self.name = name
        self.player_cards_amount = player_cards_amount
        self.cards_player_list = []

    def __str__(self):
        # print player object name and his cards.
        return f" {self.name},player cards: {self.cards_player_list}"

    def set_hand(self, deck: DeckOfCards):
        # the player get the amount of cards that he should, (10-26 cards) .
        for i in range(self.player_cards_amount):
            self.add_card(deck.del_one())

    def get_card(self):
        # get a random card  and deletes it.
        card_out = self.cards_player_list.pop(randint(0, len(self.cards_player_list) - 1))
        return card_out

    def add_card(self, card: Card):
        # add a card to your hand.
        self.cards_player_list.append(card)
