from Card_Class import Card
from random import randint
from DeckOfCards_Class import DeckOfCards


class Player:
    def __init__(self, name: str, player_cards_amount = 26):
        if type(name)!=str:
            name = "player1"
        if type(player_cards_amount)!= int:
            player_cards_amount = 26
        if 10 > player_cards_amount or player_cards_amount > 26:
            player_cards_amount = 26

        self.name = name
        self.player_cards_amount = player_cards_amount
        self.cards_player_list = []



# the player get the amount of cards that he should :  10-26 cards :)
    def set_hand(self,deck:DeckOfCards):

        for i in range (self.player_cards_amount):
            self.cards_player_list.append(deck.del_one())


#get a random card  and deletes it

    def get_card(self):
        card_out = self.cards_player_list.pop(randint(0, len(self.cards_player_list) - 1))
        return card_out
#add a card to your hand
    def add_card(self, card : Card):
        self.cards_player_list.append(card)



