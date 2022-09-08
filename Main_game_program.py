from DeckOfCards_Class import DeckOfCards
from Player_class import Player
from CardGame_class import Cardgame
from Card_Class import Card

player_name_1 = input("enter your name ")
player_name_2 = input("enter your name ")
player_1 = Player(player_name_1)
player_2 = Player(player_name_2)
if player_2.name == "player1":
    player_2.name = "player2"

# new object of new game
game = Cardgame(player_1, player_2)
# new deck cards for game
deck_game_cards:DeckOfCards = game.deck_game

# print the details of each player and his cards

deck_card_player1=game.player1.cards_player_list
deck_card_player2=game.player2.cards_player_list
print(f"the cards of {player_1.name}:{deck_card_player1}")
print(f"the cards of {player_2.name}:{deck_card_player2}")
count_win_player1 = 0
count_win_player2 = 0
for i in range(10):
    card_player1:Card = game.player1.get_card()
    card_player2:Card = game.player2.get_card()



    print(f"""round : {i+1}
""")
    print("the card of:" ,{player_1.name},card_player1)
    print("the card of:",{player_2.name},card_player2)
    if card_player1 > card_player2:
        game.player1.add_card(card_player2)
        game.player1.add_card(card_player1)
        count_win_player1+=1
        print(f"""the winner in this round is:{player_1.name}
""")
    else:
        game.player2.add_card(card_player1)
        game.player2.add_card(card_player2)
        count_win_player2 += 1
        print(f"""the winner in this round is:{player_2.name}

""")

if count_win_player1>count_win_player1:
    print(f"the winner in game is ....{player_1.name}, he winner in {count_win_player2} rounds!")
    print(f"the cards of {player_1.name}:,{game.player1.cards_player_list}")

elif count_win_player1==count_win_player2:
    print(f"oopss today its draw!")
else:
    print(f"the winner in the game is.... {player_2.name}, he winner in {count_win_player1} rounds!")
    print(f"the cards of {player_2.name}:,{game.player2.cards_player_list}")




####oriel king









