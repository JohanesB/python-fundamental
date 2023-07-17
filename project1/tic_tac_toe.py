## the board should be printed out every time a player makes a move
## accept input of the player position & place a symbol on the board

# player1 = : do you want to be X or O?
# player1 will go first
# -> are you ready to play? enter yes or no
# -> choose your next position: (1-9)
"""
# to clear the screen b/n moves
from Ipython.display import clear_output
clear_output() or 
print ('\n' * 100)


def display_board(board):
def player_input()
def place_marker(board, marker, position)
def win_check(board, mark)
import random
def choose_first()
def space_check(board, position)
def full_board_check(board)
def player_choice(board)
def replay()

"""


def display_board(board):
    print ('\n' * 100)
    print("--", "---", "---", "--")
    print("  |", "  |", "  |")
    print(board[7], "|", board[8], "|", board[9], "|")
    print("  |", "  |", "  |")
    print("--", "---", "---", "--")
    print("  |", "  |", "  |")
    print(board[4], "|", board[5], "|", board[6], "|")
    print("  |", "  |", "  |")
    print("--", "---", "---", "--")
    print("  |", "  |", "  |")
    print(board[1], "|", board[2], "|", board[3], "|")
    print("  |", "  |", "  |")
    print("--", "---", "---", "--")

def player_input():
    markr = ""
    while markr != "X" and markr != "O":
        markr = input("Player 1: Choose X or O: ").upper()

        if markr != "X" and markr != "O":
            print("Wrong input, Plaease Try again!!")

    if markr == 'X':
        return ("X", "O")
    else:
        return ("O", "X")

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[7] == mark and board[4] == mark and board[1] == mark) or
           (board[8] == mark and board[5] == mark and board[2] == mark) or
           (board[9] == mark and board[6] == mark and board[3] == mark) or
           (board[7] == mark and board[5] == mark and board[3] == mark) or
           (board[9] == mark and board[5] == mark and board[1] == mark))

import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'
    
def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1 - 9): "))
    return position
    

def replay():
    choice = input("Play again? Enter Yes or No: ")
    return choice == "Yes"

print("Welcome to Tic Tac Toe")

while True:
    my_list = [" "]*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n? ")
    if play_game == "y":
        game_on = True
    else:
        break
    
    while game_on:
        if turn == "player 1":
            display_board(my_list)

            position = player_choice(my_list)
            place_marker(my_list, player1_marker, position)

            if win_check(my_list, player1_marker):
                
                display_board(my_list)
                print("PLAYER 1 HAS WON!!")
                game_on = False
            else:
                if full_board_check(my_list):
                    display_board(my_list)
                    print("TIE GAME!!")
                    game_on = False
                    
                else:
                    turn = "player 2"


        else:
            display_board(my_list)

            position = player_choice(my_list)

            place_marker(my_list, player2_marker, position)

            if win_check(my_list, player2_marker):
                display_board(my_list)
                print("PLAYER 2 HAS WON!!")
                game_on = False
            else:
                if full_board_check(my_list):
                    display_board(my_list)
                    print("TIE GAME!!")
                    game_on = False
                    
                else:
                    turn = "player 1"

    if not replay():
        break

