from unittest import TestCase
from DeckOfCards_Class import
from Player_class import Player


class TestPlayer(TestCase):

    # set up
    def setUp(self) -> None:
        player = Player('elior', 26)

    # test the functionality of __init__
    def test__init__valid_1(self):
        player = Player('elior', 26)
        self.assertEqual(player.name, 'elior')

    # test the default name setting
    def test__init__valid_2(self):
        player = Player("", 26)
        self.assertEqual(player.name, 'player1')

    # test the way python convert int to str (from input)
    # bug?
    # def test__init__???valid???_***(self):
    #     player = Player(123, 26)
    #     self.assertEqual(player.name, '123')

    def test__init__valid_3(self):
        player = Player('elior', 26)
        self.assertEqual(player.player_cards_amount, 26)

    def test__init__valid_4(self):
        player = Player('elior', 10)
        self.assertEqual(player.player_cards_amount, 10)

    def test__init__invalid_2(self):
        player = Player('elior', 27)
        self.assertEqual(player.player_cards_amount, 26)

    def test__init__invalid_3(self):
        player = Player('elior', 9)
        self.assertEqual(player.player_cards_amount, 26)

    def test__init__invalid_4(self):
        player = Player('elior', '9')
        self.assertEqual(player.player_cards_amount, 26)

    # =========================test_set_hand==========================================
   @mock.patch('DeckOfCards_Class.DeckOfCards.del_one()', return_value = [])
    def test_set_hand_valid_1:


    def test_get_card(self):
        self.fail()

    def test_add_card(self):
        self.fail()
