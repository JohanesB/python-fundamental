import random
suits = ("Clubs", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
          "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, 
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 10}

class Card:
    def __init__(self, suits, ranks) -> None:
        self.suits = suits
        self.ranks = ranks
    def __str__(self) -> str:
        return self.ranks + " of " + self.suits
    
class Deck:
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self) -> str:
        deck_comp = ''
        for card in self.deck:
            deck_comp += ' \n' + card.__str__()
        return "The deck has: "+ deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self) -> None:
        self.cards = []  #start with an empty list as we did in the deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, card):
        # card passed in
        # from Deck.deal()
        self.cards.append(card)
        self.value += values[card.ranks]

        # Track aces
        if card.ranks == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # if total value  > 21 and i still have an aces
        # then change my ace to be a 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100) -> None:
        self.total = total
        self.bet = True

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, You do not have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)
            
        elif x[0].lower() == 's':
            print("Player Stand Dealer's Turn")
            playing = False
        else:
            print("I do not understand that, Please enter h or s only!")
            continue
        break

def show_some(player, dealer):
    # show only ONE of the dealer's card
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    # Show all (2 cards) of the player's hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # show all the dealer's card
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # print("\n Dealer's Hand: ", *dealer.cards, sep = '\n')

    # calculate and diaplay value(J+K == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")
    # Show all the player's hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.lose_bet()
def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()
def push(player, dealer):
    print('Delaer and Player tie! PUSH')




while True:
    print("WELCOME TO BLACKJACK")

    #create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up the player chips
    player_chips = Chips()

    # prompt the player for their bet
    take_bet(player_chips)

    # show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    playing = True
    while playing: # recall this variable from our hit_or_stand function
        # prompt for player to hit or stand
        playing = hit_or_stand(deck, player_hand)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # if player hand exceed 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # if player hasn't busted, play dealer's hand until dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            
            # show all cards
            show_all(player_hand, dealer_hand)

            # run different winning scenario 
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        # inform player of their chips total
        print("\n Player total chips are at: {}".format(player_chips.total))

        # Ask to play again
        new_game = input("Would you like to play another hand? y/n")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break


# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

# # PLAYER
# test_player = Hand()
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)
    
