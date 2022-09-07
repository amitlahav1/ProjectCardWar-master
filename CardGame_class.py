from Card_Class import Card
from random import randint
from DeckOfCards_Class import DeckOfCards
from Player_class import Player



class Cardgame:
    def __init__(self,player1:Player,player2:Player,player_cards_amount = 26):
        self.player1 = Player(player1,player_cards_amount)
        self.player2 = Player(player2,player_cards_amount)
        self.new_game(self.player1,self.player2)

    def new_game(self):
        if self.player1.cards_player_list==[]:
            deck_game=DeckOfCards()
            deck_game.cards_shuffle()
            self.player1.set_hand(deck_game)
            self.player2.set_hand(deck_game)
        else:
            print("the game already start")

    def get_winner(self):
        if self.player1.cards_player_list> self.player2.cards_player_list:
            winner=self.player1
            return winner
        elif self.player1.cards_player_list< self.player2.cards_player_list:
            winner=self.player2
            return winner
        else:
            return None