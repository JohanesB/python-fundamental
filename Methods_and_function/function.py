#def keyword - allow us to create function

def print_hello():
    print("Hello")
print_hello()

#taking an argument
def hello(name = "Guest"):
    print("hello {}".format(name))

hello("yohanes")
hello()

#use return keyword
def add_num(num1, num2):
    return num1 + num2
result = add_num(10, 58)
print(result)
#check even number

def check_even(number):
    result = number % 2 == 0
    return result
print(check_even(52))
print(check_even(53))

#return true any number is even inside a list
'''my_list = [1, 2, 3, 4, 5, 6]
def check_even_list(num):
    if(num % 2 == 0):
        return True
    else:
        pass
for number in my_list:
    print(check_even_list(number)) '''

'''def check_even_list(num):
    for number in num:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([1, 3, 5]))
print(check_even_list([1, 2, 3, 4, 5]))'''

# instead of return true or false print each even number
even_numbers = []
def check_even_list(num):
    for number in num:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

even_numbers = check_even_list([1, 2, 3, 4, 5, 6])
print(even_numbers)

# Tuple unpacking with function
work_hours = [("abi", 100), ("Bini", 900), ("Dani", 500)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)
result = employee_check(work_hours)
print(result)
name, hours = employee_check(work_hours)
print(name)
print(hours)

# interaction between python function

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from random import shuffle
shuffle(my_list) # not assigned on variable
print(my_list)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
shuffle_list = shuffle_list(my_list)
print(shuffle_list)