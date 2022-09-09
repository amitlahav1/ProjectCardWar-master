from unittest import TestCase
from DeckOfCards_Class import DeckOfCards
from Player_class import Player
from CardGame_class import Cardgame
from Card_Class import Card


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

    # the len of deck equal. p1,p2 get one card to the list .valid
    def test_get_winner_equal_valid_1(self):
        p1 = Player("amit")
        p2 = Player("elior")
        card = Card('Diamond', 12)
        card2 = Card('Diamond', 7)
        game = Cardgame(p1, p2)
        game.player1.cards_player_list=[card]
        game.player2.cards_player_list=[card2]
        self.assertEqual(game.get_winner(), None)

    # player 1 get 2 card. player2 1. player1 need to be winner
    def test_get_winner_player1_bigger_valid_2(self):
        player_1 = Player("amit")
        player_2 = Player("elior")
        card = Card('Diamond', 12)
        card2 = Card('Diamond', 7)
        game = Cardgame(player_1, player_2)
        game.player1.cards_player_list = [card, card2]
        game.player2.cards_player_list = [card]
        self.assertEqual(game.get_winner(), game.player1)

    # player2 get 2 card , player1 get 1 card . player 2 need to be winner
    def test_get_winner_player2_valid_3(self):
        player_1 = Player("amit")
        player_2 = Player("elior")
        card = Card('Diamond', 12)
        card2 = Card('Diamond', 7)
        game = Cardgame(player_1, player_2)
        game.player1.cards_player_list = [card]
        game.player2.cards_player_list = [card, card2]
        self.assertEqual(game.get_winner(), game.player2)

    # player 1 with one card. player 2 with two card. player2 need to be winner
    def test_get_winner_invalid_1(self):
        player_1 = Player("amit")
        player_2 = Player("elior")
        card = Card('Diamond', 12)
        card2 = Card('Diamond', 7)
        game = Cardgame(player_1, player_2)
        game.player1.cards_player_list = [card]
        game.player2.cards_player_list = [card, card2]
        self.assertNotEqual(game.get_winner(), game.player1)

    # player 1 with two card. player 2 with one card. player1 need to be winner
    def test_get_winner_invalid_2(self):
        player_1 = Player("amit")
        player_2 = Player("elior")
        card = Card('Diamond', 12)
        card2 = Card('Diamond', 7)
        game = Cardgame(player_1, player_2)
        game.player1.cards_player_list = [card, card2]
        game.player2.cards_player_list = [card]
        self.assertNotEqual(game.get_winner(), game.player2)
