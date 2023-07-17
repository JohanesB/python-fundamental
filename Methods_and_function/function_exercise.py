# write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def check_even(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
check = check_even(2, 4)
print(check)
check = check_even(2, 9)
print(check)

# write a function takes a two word string and returns true if both words begin with the same letter
def animal_cracker(txt):
    split_txt = txt.split()
    first = split_txt[0]
    second = split_txt[1]
    return first[0] == second[0]

check = animal_cracker("Yohanes Bacha")
print(check)

# write a function that capitalize the first and fourth letters of a name

def old_macdonal(name):
    """first_letter = name[0]
    inbetween = name[1:3]
    second_letter = [3]
    rest = name[4:]
    return first_letter.upper() + inbetween + second_letter.upper() + rest"""

    half_word = name[0:3]
    other = name[3:]
    return half_word.capitalize() + other.capitalize()
name = old_macdonal('macdonald')
print(name)

# return a sentence with the words reversed
def master_yoda(text):
    text_split = text.split()
    reversed_word_list = text_split[::-1]
    print(' '.join(reversed_word_list))
master_yoda("i am home")

# given a list of integer, return true if the array contains a 3 next to a 3 somewhere

def has_22(num):
    for i in range(0, len(num) - 1):
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False
check = has_22([1, 2, 3, 3])
print(check)
    
# write a function that takes in a list of integers and return True if it contains 0027 in order
def has_0027(args):
    check = [0, 0, 2, 7, "x"]
    for num in args:
        if(num == check[0]):
            check.pop(0)
    return len(check) == 1
checked = has_0027([1,2,3,0,3,0,2,9,7])
print(checked)