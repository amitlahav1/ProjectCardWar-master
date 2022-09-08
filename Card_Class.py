class Card:
    def __init__(self, suit: str, value: int):
        # define Card object.
        if type(suit) != str:
            raise TypeError("suit must to be type str!!!!")
        if type(value) != int:
            raise TypeError("value must to be type int!!!")
        if value <= 0 or value > 13:
            raise ValueError("value must to be between 1-13!!!")
        if suit != 'Heart' and suit != 'Spade' and suit != 'Diamond' and suit != 'Club':
            raise ValueError('suit is invalid')

        self.suit_dict = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
        self.suit = suit
        self.value = value

    def __str__(self):
        # print the card object in class Card.
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        # print the Cards in player's hand (list).
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        # make sure that the cards equalized first by value and then by suit,
        # make sure that card is Card object.
        if type(other) == Card:
            if self.value == other.value:
                if self.suit == other.suit:
                    return True
            else:
                return False

        else:
            raise TypeError("other must to be type card!!!!")

    def __gt__(self, other):
        # make sure that the cards compared first by value and then by suit,
        # make sure that card is Card object.
        if type(other) == Card:
            if self.value > other.value:
                return True
            elif self.value == other.value:
                if self.suit_dict[self.suit] > self.suit_dict[other.suit]:
                    return True
            else:
                return False
        else:
            raise TypeError("other must to be type card!!!!")
