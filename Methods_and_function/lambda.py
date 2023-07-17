# lambda expression used to quickly create anonymes function, which it is one time use function
# map function
"""def square(nums):
    return nums**2
my_nums = [1, 2, 3, 4, 5]
for items in map(square, my_nums):
    print(items)
print(list(map(square, my_nums)))"""

########
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]
names = ["Andy", "EVE", "Sally"]
print_names = list(map(splicer, names))
print(print_names)

# filter function
def check_even(num):
    return num % 2 == 0
mynums = [1, 2, 3, 4, 5, 6]
print_nums = list(filter(check_even, mynums))
print(print_nums)

##### lamda expression ####
square = lambda num : num ** 2
print(square(5))
####or####

print(list(map(lambda num: num ** 3, mynums)))

## convert the above check_even function in lamda expression

print(list(filter(lambda num: num % 2 == 0, mynums)))