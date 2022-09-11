from DeckOfCards_Class import DeckOfCards
from Player_class import Player


class Cardgame:
    # define game settings (players and rounds).
    def __init__(self, player1: Player, player2: Player, player_cards_amount=26):
        self.player1 = Player(player1, player_cards_amount)
        self.player2 = Player(player2, player_cards_amount)
        self.deck_game = DeckOfCards()
        self.new_game()

    def new_game(self,):
        # setting up new game.
        if self.player1.cards_player_list == []:
            self.deck_game.cards_shuffle()
            self.player1.set_hand(self.deck_game)
            self.player2.set_hand(self.deck_game)
        else:
            raise TypeError("the game already start")

    def get_winner(self):
        # function that check who is the winner in the game (len:player list).
        if len(self.player1.cards_player_list) > len(self.player2.cards_player_list):
            winner = self.player1
            return winner
        elif len(self.player1.cards_player_list) < len(self.player2.cards_player_list):
            winner = self.player2
            return winner
        else:
            return None
