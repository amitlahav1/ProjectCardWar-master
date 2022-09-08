from unittest import TestCase
from unittest.mock import patch
from DeckOfCards_Class import DeckOfCards
from Card_Class import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_valid = DeckOfCards()


# test that  len of deck is 52.valid
    def test_deck_len_valid_1(self):
        self.assertEqual(len(self.deck_valid.deck52),52)

# test that len of deck is 53.invalid
    def test_deck_len_invalid_1(self):
            self.assertNotEqual(len(self.deck_valid.deck52), 53)

# test that len of deck is 51.invalid
    def test_deck_len_invalid_2(self):
            self.assertNotEqual(len(self.deck_valid.deck52), 51)

# test to check that only 1 type of card in the deck. no dubles.
    def test_deck_one_card_valid_1(self):
        for i in self.deck_valid.deck52:
            self.assertEqual(self.deck_valid.deck52.count(i), 1)

# test to check that have dubles card in deck. invalid.
    def test_deck_duble_card_invalid_1(self):
        for i in self.deck_valid.deck52:
            self.assertNotEqual(self.deck_valid.deck52.count(i), 2)

#test valid.card ace need to be in deck as value 14.
    def test_ace_power_invalid_1(self):
        card_ace = Card("Spade", 14)
        card_ace_not = Card("Spade", 1)
        self.assertNotIn(card_ace_not,self.deck_valid.deck52)
        self.assertIn(card_ace,self.deck_valid.deck52)

#test that deck after the shuffle not same

    def test_cards_shuffle_valid_1(self):
        self.assertNotEqual(self.deck_valid.cards_shuffle(),self.deck_valid)

#take out from the deck  card and check that the card dont exist in the deck.valid
    def test_del_one_card_valid_1(self):
        self.assertNotIn(self.deck_valid.del_one(),self.deck_valid.deck52)

#chek if the function del return the card. valid
    def test_return_card_del_valid_2(self):
        card_1 = Card("Spade", 5)
        with patch ('DeckOfCards_Class.DeckOfCards.del_one') as mock_card:
            mock_card.return_value = card_1
            self.assertEqual(self.deck_valid.del_one(), card_1)
