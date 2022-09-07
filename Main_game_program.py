from DeckOfCards_Class import DeckOfCards
from Player_class import Player
from CardGame_class import Cardgame

player_name_1 = input("enter your name ")
player_name_2 = input("enter your name ")

player_1 = Player(player_name_1)
player_2 = Player(player_name_2)

# new object,new shuffled deck for new game.
maindeck = DeckOfCards()
maindeck.cards_shuffle()

# new object of new game
game = Cardgame(player_1, player_2)
# game.new_game()



# print the details of each player and his cards

deck_card_player1=game.player1.cards_player_list
deck_card_player2=game.player2.cards_player_list
print(f"the cards of {player_name_1}:{deck_card_player1}")
print(f"the cards of {player_name_2}:{deck_card_player2}")

count_win_player1 = 0
count_win_player2 = 0
for i in range(10):
    card_player1 = game.player1.get_card
    card_player2 = game.player2.get_card
    print(f"""round : {i+1}
""")
    print("the card of:" ,{player_name_1},game.player1.get_card())
    print("the card of:",{player_name_2},game.player2.get_card())
    if game.player1.get_card() > game.player2.get_card():
        game.player1.add_card(game.player2.get_card())
        game.player1.add_card(game.player1.get_card())
        count_win_player1+=1
        print(f"""the winner in this round is:{player_name_1}

""")
    else:
        game.player2.add_card(game.player1.get_card())
        game.player2.add_card(game.player2.get_card())
        count_win_player2 += 1
        print(f"""the winner in this round is:{player_name_2}

""")

if count_win_player1>count_win_player1:
    print(f"the winner in game is ....{player_name_1}")
elif count_win_player1==count_win_player2:
    print(f"oopss today its draw!")
else:
    print(f"the winner in the game is.... {player_name_2}")











#skdskdjksjdksjdjskjsksjkjskjsk








