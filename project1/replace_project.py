##  choose the position in the list and replace a value

def display(game_lst):
    print("here is the current list: ")
    print(game_lst)

def position_choice():
    choice = "wrong"
    
    while choice not in ["0", "1", "2"]:
        choice = input("Pick position (0, 1, 2): ")

        if choice not in ["0", "1", "2"]:
            print("Sorry, invalid choice!")
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = "wrong"
    
    while choice not in ["Y", "N"]:
        choice = input("keep playing? (Y or N): ")

        if choice not in ["Y", "N"]:
            print("Sorry, I dont understand, Please choose Y or")
    
    if choice == "Y":
        return True
    else:
        return False

game_list = [1, 2, 3]
game_on = True

while game_on:
    display(game_list)
    position = position_choice()
    replacement_choice(game_list, position)
    display(game_list)
    game_on = gameon_choice()
