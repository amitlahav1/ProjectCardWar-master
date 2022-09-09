from unittest import TestCase
from Card_Class import Card


class TestCard(TestCase):
    def setUp(self):
        # this is a valid card!
        self.card = Card('Diamond', 12)
        self.card1 = Card('Club', 3)

    # a valid test case for proper function of __init__
    def test__init__valid_1(self):
        self.assertEqual(self.card.value, 12)
        self.assertEqual(self.card.suit, 'Diamond')

    # a valid test case for proper suit and value inside an object in class Card
    def test__init__valid_2(self):
        self.assertEqual(type(self.card.value), int)
        self.assertEqual(type(self.card.suit), str)

    # an invalid test case for non-proper value (type) inside an object in class Card
    def test__init__invalid_2(self):
        with self.assertRaises(TypeError):
            Card('Diamond', 'str')

    # a invalid test case for non-proper value (value) inside an object in class Card
    def test__init__invalid_3(self):
        with self.assertRaises(ValueError):
            Card('Diamond', 15)
        with self.assertRaises(ValueError):
            Card('Diamond', -1)

    # a valid test case for Extreme case 'value' inside an object in class Card
    def test__init__valid_3(self):
        card = Card('Diamond', 1)
        self.assertEqual(card.value, 1)

    # a valid test case for Extreme case 'value' inside an object in class Card
    def test__init__valid_4(self):
        card = Card('Diamond', 13)
        self.assertEqual(card.value, 13)

    # a valid test case for ACE card 'value' inside an object in class Card
    def test__init__valid_5(self):
        card = Card('Diamond', 14)
        self.assertEqual(card.value, 14)

    # ========================================test cases for suit===================================================#

    # a valid test case for suit options inside an object in class Card
    def test__init__valid_6(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Spade', 13)
        card3 = Card('Heart', 13)
        card4 = Card('Club', 13)
        self.assertEqual(card1.suit, 'Diamond')
        self.assertEqual(card2.suit, 'Spade')
        self.assertEqual(card3.suit, 'Heart')
        self.assertEqual(card4.suit, 'Club')

    # an invalid test case for suit options inside an object in class Card
    def test__init__invalid_4(self):
        with self.assertRaises(ValueError):
            Card('str', 13)

    # an invalid test case for non-proper suit inside an object in class Card
    def test__init__invalid_1(self):
        with self.assertRaises(TypeError):
            Card(123, 10)

    #####################################################################################

    # check if the __eq__ function works appropriate with values
    def test__eq__valid_1(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Club', 13)
        self.assertTrue(card1.value == card2.value)

    # check if the __eq__ function works appropriate with suits
    def test__eq__valid_2(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Diamond', 12)
        self.assertTrue(card1.suit == card2.suit)

    # check if the __eq__ function works appropriate with uneven card values
    def test__eq__invalid_1(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Club', 12)
        self.assertFalse(card1.value == card2.value)

    ##############################################################################

    # check if the __gt__ function works appropriate with different values
    def test__gt__valid_1(self):
        card1 = Card('Diamond', 13)  # high card
        card2 = Card('Diamond', 12)
        self.assertTrue(card1.value > card2.value)

    # check if the __gt__ function works appropriate with suits
    def test__gt__valid_2(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Club', 13)  # high card
        self.assertTrue(card2 > card1)

    # check if the __gt__ function works appropriate with suits (invalid)
    def test__gt__invalid_1(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Club', 13)  # high card
        self.assertFalse(card1 > card2)

    # check if the __gt__ function works appropriate with suits
    def test__gt__invalid_2(self):
        card1 = Card('Diamond', 13)
        card2 = Card('Club', 13)  # high card
        self.assertFalse(card1.value > card2.value)
