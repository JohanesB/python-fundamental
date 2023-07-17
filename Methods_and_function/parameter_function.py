# parameter of function include argument(*args) and keyword argument(**kwargs)
# *args - allow us to take an arbitrary number of argument and return as a tupel
# **kwargs - allow us to take an arbitrary number of argument and return as a dictionary key value pairs
'''def func(a, b, c=0, d=0, e=0):
    return sum((a, b, c, d, e)) * 0.05
addition = func(25, 56) # the argument in this function call is positional argument
print(addition)'''

def func(*args):
    return sum(args) * 0.05
addition = func(54, 54, 12)
print(addition)

# **kwargs examples
def func(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("my favorite fruite is {}".format(kwargs["fruit"]))
    else:
        print('i did not find any fruit here')

func(fruit = "banana", vegitable = "lettuce")

# lets combine these two argument

def comb(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} glass of {}".format(args[0], kwargs["drink"]))
comb(1, 2, 3, food = "eggs", drink = "wine", fruit = "orange")