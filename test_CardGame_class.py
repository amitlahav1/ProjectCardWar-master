from unittest import TestCase, mock
from DeckOfCards_Class import DeckOfCards
from Player_class import Player
from unittest.mock import patch
from CardGame_class import Cardgame


class TestCardgame(TestCase):

    def test_setUp(self):
        self.deck_cards = DeckOfCards()
        self.game = Cardgame("amit", "elior", 26)

    # test init valid. the game get valid argument
    def test_init_valid_1(self):
        self.game = Cardgame("amit", "elior", 26)

        self.assertEqual(len(self.game.player1.cards_player_list), 26)
        self.assertEqual(self.game.player1.name, "amit")
        self.assertEqual(self.game.player2.name, "elior")

    # test init valid.the game get valid argument
    def test_init_valid_2(self):
        self.game = Cardgame("", "")
        self.assertEqual(self.game.player1.name, "player1")
        self.assertEqual(self.game.player2.name, "player1")

    # player_cards_amount>26. defult =26. the game get the correctly arguments
    def test_init_invalid_1(self):
        self.game = Cardgame("", "", 27)
        self.assertEqual(len(self.game.player1.cards_player_list), 26)

    # test to amount card is 15, player 1 =15 cards.the game get the correctly arguments
    def test_init_valid_3(self):
        self.game = Cardgame("", "", 15)
        self.assertEqual(len(self.game.player1.cards_player_list), 15)
        self.assertEqual(len(self.game.player2.cards_player_list), 15)

    # player_cards_amount<10. defult =26. the game get the correctly arguments
    def test_init_invalid_2(self):
        self.game = Cardgame("", "", 5)
        self.assertEqual(len(self.game.player1.cards_player_list), 26)

    # after the cards are dealt, the players' decks should be equal
    def test_new_game_valid_1(self):
        self.game = Cardgame("amit", "elior", 26)
        p1_len = len(self.game.player1.cards_player_list)
        p2_len = len(self.game.player2.cards_player_list)
        self.assertTrue(p1_len == p2_len)

    # after the cards are dealt, the players' decks should be equal
    def test_new_game_valid_1(self):
        self.game = Cardgame("amit", "elior", 12)
        p1_len = len(self.game.player1.cards_player_list)
        p2_len = len(self.game.player2.cards_player_list)
        self.assertTrue(p1_len == p2_len)

    # the len of deck id equal. valid
    def test_get_winner_equal_valid_1(self):
        self.p1 = Player("amit")
        self.p2 = Player("elior")
        self.game = Cardgame(self.p1, self.p2)
        self.assertTrue(self.game.get_winner(), "none")

    # player 1 get one card. player2 zero
    def test_get_winner_player1_bigger_valid_2(self):
        self.game.player1.cards_player_list = ["Spade", 3]
        self.assertNotEqual(self.game.get_winner(), self.game.player2)

