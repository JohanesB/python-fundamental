## write a function that computes the volume of sphere given it's radius
from math import pi
def vol(rad):
    return 4/3 * pi * rad**3
print(vol(2))

## write a function that checks whether a number is in a given range(inclusive of high or low)
def ran_check(num, low, high):
    if num in range(low, high):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not in the range of {low} and {high}")
ran_check(5, 4, 7)

## alternative way to return a boolean

def ran_bool(num, low, high):
    if num in range (low, high):
        return True
    else:
        return False
test = ran_bool(3, 1, 10)
print(test)

## write a python function that accept a string and calculates the number of upper case letters and lower case letters

def up_low(s):
    print(f"original String: {s}")
    upper = []
    lower = []
    split = s.split()
    print(split)
    for str in split:
        for st in str:
            if st.isupper():
                upper.append(st)
            elif st.islower():
                lower.append(st)
    print(f"Number of Upper case characters: {len(upper)}")
    print(f"Number of Lower case characters: {len(lower)}") 
s = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_low(s)

## write a python function that takes a list and returns a new list with unique elements of the first list

def unique_list(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    print(unique)
unique_list([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5])

# write a python function to multiply all the numbers in a list

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    print(f"the result is {result}")
multiply([1, 2, 3, -4])

##  write a python function that checks whether a word or phrase is palindrome or not
def palindrome(s):
    txt = s.replace(" ", "")
    if txt == txt[::-1]:
        return True
    else:
        return False
check_palindrome = palindrome("helleh")
print(check_palindrome)

## write a python function to check whether a string is panagram or not
# panagrams are words or sentences containing every letter of the alphabet at least once

import string
def ispanagram(str1, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    sentence = str1.lower()
    sentence1 = sentence.replace(" ", "")
    letter = set(sentence1)
    
    if letter == alphabet:
        return True
    else:
        return False 

check = ispanagram("the quick brown fox jumps over the lazy dog")
print(check)