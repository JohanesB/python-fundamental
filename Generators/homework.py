# create a generator that generates the squares of numbers up to some number N

def gensquares(N):
    for y in range(N):
        yield y**2

for x in gensquares(10):
    print(x)

# use the iter() function to convert the string below into iterator

s = 'hello'
s = iter(s)
print(next(s))

# create a generators that yields "n" random numbers between low and high number (that are inputes) 

import random
def rand_num(low, high, num):
    for x in range(num):
        yield random.randint(low, high)

for num in rand_num(1, 100, 12):
    print(num)