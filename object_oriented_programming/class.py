class Dog():
    def __init__(self, breed, color, sex):
        # Attributes
        # we take in the argument
        # assign it using self.attribute_name
        self.dog_type = breed
        self.color = color
        self.sex = sex

my_dog = Dog(breed='shepherd', color="black", sex="male")
print("my dog type is "+my_dog.dog_type + " and the color is " + my_dog.color)

class Employee():
    def __init__(self, name, sex, age, department, position) -> None:
        self.name = name
        self.sex = sex
        self.age = age
        self.department = department
        self.position = position

Employee1 = Employee(name="Amir", sex="Male", age="34", department="inrusion", position="professional")
print(Employee1.name + " age is " + Employee1.age)