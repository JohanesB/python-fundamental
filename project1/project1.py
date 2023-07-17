def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

## displaying information
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
"""result = input("please enter a value: ")
position_index = int(input("choose an index position: "))
row1[position_index] = result"""


# validating user input

def user_choice():
    choice = "wrong"
    acceptable_value = range(0, 3)
    within_range = False
    result = input("please enter a value: ")

    while choice.isdigit() == False or within_range == False:
        choice = input("choose an index position (0, 2): ")
        #digit check
        if choice.isdigit() == False:
            print("sorry thart is not a digit, Please Try again")
        
        #RANGE CHECK

        if choice.isdigit() == True:
            if int(choice) in acceptable_value:
                within_range = True
            else:
                within_range = False
                print("the input must be in range of (0 - 2), please try again")
    row1[int(choice)] = result
user_choice()
display(row1, row2, row3)