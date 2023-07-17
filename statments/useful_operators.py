for num in range(10):
    print(num)
print("print from number 4 upto 10")
for num in range(4, 10):
    print(num)
print("print from number 0 upto 10 within 2 range")
for num in range(0, 10, 2):
    print(num)

# generator function is generate information instead of savin in a memory
print(list(range(0, 20, 3)))

#enumeration - it is a function that take in any iterable object and returns index counter and object itself
index_count = 0
for item in "yohanes":
    print("in index {} there is a character {}".format(index_count, item))
    index_count += 1
# or

index_count = 0
letter = "yohanes"
for item in letter:
    print(letter[index_count])
    index_count += 1
# to enumerate this

index_count = 0
letter = "yohanes"
for item in enumerate(letter):
    print(item)

# zip function - zipps(combines) two or more objects and pairs up this objects so that they much together

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)

# 'in' keyword operator - to to quickly check smtg
print(0 in [1, 2, 3])
print("key1" in {"key1": 23})
print("yo" in "yohanes")

# min and max function
list3 = [10, 20, 30, 100]
print(min(list3))
print(max(list3))

# random library - it's not returning anything, just shuffle
from random import shuffle

list4 = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(list4)
print(list4)

from random import randint

print(randint(0, 100))

# to accept a result from a keyword - always return a string
result = input("enter a result here: ")
print(result)
result = int(input("enter a result here: "))