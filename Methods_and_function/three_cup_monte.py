# this is a guessing game which is called "Three Cup Monte"
def player_guess():
    guess = ''
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2 \n")
    return int(guess)
def check_guess(mylist, guess):
    if mylist[guess] == "*":
        print("Correct Guess")
        print(mylist)
    else:
        print("Wrong Guess")
        print(mylist)
# INITIAL LIST
my_list = [' ', '*', '']
print("list is {}".format(my_list))
# SHUFFLE LIST
from random import shuffle
shuffle(my_list)
# USER GUESS
guess = player_guess()
# CHECK GUESS
check_guess(my_list, guess)