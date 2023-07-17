# def hello():
#     return "Hello!"

# print(hello())
# greet = hello
# print("this is from greet "+ greet())
# print(greet)
# del hello
# # print(hello)
# print("this is from greet "+ greet())

def hello(name = "Jose"):
    print('the hello() function has been executed!')

    def greet():
        return "\t this is the greet() func inside hello"
    def welcome():
        return "\t this is the welcome() inside hello"
    # print(greet())
    # print(welcome())
    # print("This is the end of hello function!")
    if name == 'Jose':
        return greet()
    else:
        return welcome

my_new_func = hello('Jose')
print(my_new_func)


def hi():
    print("Hi JO")
def other(some_def_func):
    print("other code runs here!!")
    print(some_def_func())
other(hi)



def new_decorator(original_func):
    def wrap_func():
        print("some extra code, before the original function")
        original_func()
        print("some extra code, after the original function")
    
    return wrap_func

@new_decorator
def func_needs_decorated():
    print("i want to be decorated")

# decorated_funce = new_decorator(func_needs_decorated)
# print(decorated_funce())

print(func_needs_decorated())