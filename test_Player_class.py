from unittest import TestCase, mock
from DeckOfCards_Class import DeckOfCards
from Player_class import Player
from Card_Class import Card


class TestPlayer(TestCase):

    # set up
    def setUp(self):
        self.player = Player('elior', 26)
        self.deck52 = DeckOfCards()

    # test the functionality of __init__
    def test__init__valid_1(self):
        player = Player('elior', 26)
        self.assertEqual(player.name, 'elior')

    # test the default name setting
    def test__init__valid_2(self):
        player = Player("", 26)
        self.assertEqual(player.name, 'player1')

    # test the way python convert int to str (from input)
    def test__init__valid_(self):
        player = Player(123, 26)
        self.assertEqual(player.name, 123)

    #  test extreme case
    def test__init__valid_3(self):
        player = Player('elior', 26)
        self.assertEqual(player.player_cards_amount, 26)

    #  test extreme case
    def test__init__valid_4(self):
        player = Player('elior', 10)
        self.assertEqual(player.player_cards_amount, 10)

    # test invalid case
    def test__init__invalid_2(self):
        player = Player('elior', 27)
        self.assertEqual(player.player_cards_amount, 26)

    # test invalid case
    def test__init__invalid_3(self):
        player = Player('elior', 9)
        self.assertEqual(player.player_cards_amount, 26)

    # test that if the got str then set default 26
    def test__init__invalid_4(self):
        player = Player('elior', '9')
        self.assertEqual(player.player_cards_amount, 26)

    # =========================test_set_hand========================================== #

    # test the amount of cards that this function gives to this player
    #  and that he pops a card out of the main deck
    @mock.patch('DeckOfCards_Class.DeckOfCards.del_one', return_value=('Diamond', 2))
    def test_set_hand_valid_1(self, del_mock):
        self.player.set_hand(self.deck52)
        self.assertTrue(('Diamond', 2) in self.player.cards_player_list)
        self.assertEqual(len(self.player.cards_player_list), self.player.player_cards_amount)

    # test the amount of cards that this function gives to this player
    #  and that he pops a card out of the main deck (invalid)
    @mock.patch('DeckOfCards_Class.DeckOfCards.del_one', return_value=('Diamond', 2))
    def test_set_hand_invalid_1(self, del_mock):
        self.player.set_hand(self.deck52)
        self.assertFalse(('Diamond', 5) in self.player.cards_player_list)
        self.assertEqual(len(self.player.cards_player_list), self.player.player_cards_amount)

    # =======================================test_get_card================================= #

    # make sure that the function picks a card and deletes it from players hand
    def test_get_card_valid_1(self):
        self.player.set_hand(self.deck52)
        start_hand = len(self.player.cards_player_list)
        self.player.get_card()
        after_turn_hand = len(self.player.cards_player_list)

        self.assertEqual(after_turn_hand + 1, start_hand)
        self.assertNotIn(self.player.get_card(), self.player.cards_player_list)

    # ===============================test_add_card====================================== #
    def test_add_card_valid_1(self):
        card = Card('Club', 8)
        self.player.add_card(card)
        self.assertIn(card, self.player.cards_player_list)

    def test_add_card_invalid_1(self):
        card = Card('Club', 8)
        card1 = Card('Club', 4)
        self.player.add_card(card)
        self.assertNotIn(card1, self.player.cards_player_list)
