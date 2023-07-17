# inheritance is a way to form a new classes using classes that have already been defined
# used for reusing of the code

class Animal():
    def __init__(self) -> None:
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("i am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self) -> None:
        Animal.__init__(self)
        print("DOG CREATED")
    
    def who_am_i(self):   # override method
        print("I am a Dog!!")

my_dog = Dog()
print(my_dog.eat())
print(my_dog.who_am_i())