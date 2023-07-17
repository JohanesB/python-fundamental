# suits = clubs, diamonds, spades, clubs
# rank = values.key
import random
suits = ("Clubs", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
          "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, 
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self) -> str:
        return 
    
class Deck:
    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #list of single card object
            self.all_cards.append(new_cards)
    
    def __str__(self) -> str:
        return f"player {self.name} has {len(self.all_cards)} cards"
        

# three_of_clubs = Card("dimonds", "Three")
# print(three_of_clubs)
# two_of_clubs = Card("spades", "Jack")
# print(two_of_clubs)
# print(three_of_clubs.value > two_of_clubs.value)

# new_deck = Deck()
# first_card = new_deck.all_cards[0]
# print(first_card)
# for card_object in new_deck.all_cards:
#     print(card_object)

# new_deck.shuffle()
# print(new_deck.deal_one())
# print(len(new_deck.all_cards))

# new_player = Player("JO")
# print(new_player)
# new_player.add_cards(two_of_clubs)
# print(new_player)

#GAME SETUP
player_one = Player("One")
player_two = Player("Two")
#
#creating a deck
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, Out of cards! Player Two Wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, Out of cards! Player One Wins!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    at_war = True
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 3:
                print("Player One unable to Declare War")
                print("PLAYER TWO WINS!")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player Two unable to Declare War")
                print("PLAYER ONE WINS!")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
