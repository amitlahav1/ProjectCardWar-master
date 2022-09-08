from unittest import TestCase

import Card_Class
import Player_class
from DeckOfCards_Class import DeckOfCards
from Player_class import Player
from unittest.mock import patch
from CardGame_class import Cardgame


class TestCardgame(TestCase):

    def test_setUp(self):
        self.deck_cards = DeckOfCards()

#test init valid. the game get valid argument
    def test_init_valid_1(self):
        self.game = Cardgame("amit","elior",26)

        self.assertEqual(len(self.game.player1.cards_player_list),26)
        self.assertEqual(self.game.player1.name,"amit")
        self.assertEqual(self.game.player2.name,"elior")

#test init valid.the game get valid argument
    def test_init_valid_2(self):
        self.game = Cardgame("","")
        self.assertEqual(self.game.player1.name,"player1")
        self.assertEqual(self.game.player2.name,"player1")

# player_cards_amount>26. defult =26. the game get the correctly arguments
    def test_init_invalid_1(self):
        self.game = Cardgame("", "",27)
        self.assertEqual(len(self.game.player1.cards_player_list),26)

# test to amount card is 15, player 1 =15 cards.the game get the correctly arguments
    def test_init_valid_3(self):
        self.game = Cardgame("", "", 15)
        self.assertEqual(len(self.game.player1.cards_player_list), 15)
        self.assertEqual(len(self.game.player2.cards_player_list),15)

 #player_cards_amount<10. defult =26. the game get the correctly arguments
    def test_init_invalid_2(self):
         self.game = Cardgame("", "",5)
         self.assertEqual(len(self.game.player1.cards_player_list), 26)

#after the cards are dealt, the players' decks should be equal
    def test_new_game_valid_1(self):
        self.game = Cardgame("amit","elior",26)
        p1_len=len(self.game.player1.cards_player_list)
        p2_len=len(self.game.player2.cards_player_list)
        self.assertTrue(p1_len == p2_len)

# after the cards are dealt, the players' decks should be equal
    def test_new_game_valid_1(self):
        self.game = Cardgame("amit", "elior", 12)
        p1_len = len(self.game.player1.cards_player_list)
        p2_len = len(self.game.player2.cards_player_list)
        self.assertTrue(p1_len == p2_len)


    def test_get_winner(self):
        with patch () as mock_card:
            mock_card.return_value = card_1
