class Card:
    def __init__(self, suit: str, value: int):

        if type(suit) != str:
            raise TypeError ("suit must to be type str!!!!")
        if type(value) != int:
            raise TypeError("value must to be type int!!!")
        if value <=0 or value>13:
            raise ValueError("value must to be between 1-13!!!")
        if suit != 'Heart' and suit != 'Spade' and suit != 'Diamond' and suit != 'Club':
            raise ValueError('suit is invalid')

        self.suit_dict = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        if type(other) == Card:
            if self.value == other.value:
                if self.suit == other.suit:
                    return True
            else:
                return False

        else:
            raise TypeError("other must to be type card!!!!")


    def __gt__(self, other):
        if self.value==1:
            self.value=14
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


# h2 =Card('Heart', 2)
# c2 =Card('Club', 2)

# if c2> h2:
#     print(c2)