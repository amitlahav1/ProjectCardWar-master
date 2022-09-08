from unittest import TestCase
from Card_Class import Card


class TestCard(TestCase):
    def setUp(self):
        self.card = Card('Diamond', 12)
        print('setUp')

    def tearDown(self):
        print('tearDown')

# a valid test case for proper function of __init__
    def test__init__valid_1(self):
        self.assertEqual(self.card.value, 12)
        self.assertEqual(self.card.suit, 'Diamond')

# a valid test case for proper suit and value inside an object in class Card
    def test__init__valid_2(self):
        self.assertEqual(type(self.card.value), int)
        self.assertEqual(type(self.card.suit), str)

# a invalid test case for non-proper suit inside an object in class Card
    def test__init__invalid_1(self):
         with self.assertRaises(TypeError):
             Card(123, 10)

# a invalid test case for non-proper value (type) inside an object in class Card
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
#========================================test cases for suit===================================================#

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

# a invalid test case for suit options inside an object in class Card
    def test__init__invalid_4(self):
        with self.assertRaises(ValueError):
            Card('str', 13)


