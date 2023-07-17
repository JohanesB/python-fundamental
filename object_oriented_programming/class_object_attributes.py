class Dog():

    #class object attributes
    # same for any instance

    species = "mammals"
    def __init__(self, name, breed, color, sex):
        # Attributes
        # we take in the argument
        # assign it using self.attribute_name
        self.name = name
        self.dog_type = breed
        self.color = color
        self.sex = sex

        # OPERATION/action ----> method

    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog(name="Kodi", breed='shepherd', color="black", sex="male")
print("my dog type is "+my_dog.dog_type + " and the color is " + my_dog.color)
print(my_dog.bark(25))


class Circle():
    PI = 3.14

    def __init__(self, radius = 1) -> None:
        self.radius = radius
        self.area = radius*radius*self.PI # or Circle.PI

    def get_circumference(self):
        return self.radius * self.PI * 2
my_circle = Circle(radius=34)
print("the circumference of the given circle is " + str(my_circle.get_circumference()) + " and the area is " + str(my_circle.area))