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

    def __str__(self):
        return f"player hand{self.cards_player_list},main deck : {DeckOfCards.__str__(d)} "

# the player get the amount of cards that he should :  10-26 cards :)
    def set_hand(self,deck:DeckOfCards):

        for i in range (self.player_cards_amount):
            self.cards_player_list.append(d.del_one())


#get a random card  and deletes it

    def get_card(self):
        card_out = self.cards_player_list.pop(randint(0, len(self.cards_player_list) - 1))
        return card_out
#add a card to your hand
    def add_card(self, card : Card):
        self.cards_player_list.append(card)



# d = DeckOfCards()
# player1 = Player('amit', 15)
# player2 = Player('elior', 26)
#
# d.cards_shuffle()
# print(player1.set_hand(d))
# print(d)
# print(player1.get_card())
# print(player1.cards_player_list)
# player2.add_card()
