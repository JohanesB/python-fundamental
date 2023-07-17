# continue to execute a block of code while some condition remains true
# syntax of while loop
# while some_boolean_condition:
   #do something
x = 0
while x < 5:
    print(f"the current value of x is {x}")
    x = x + 1
else:
    print(f"x is not less than {x}")

# break: breaks out of the current closest enclosing loop
# continue: goes to the top of the closest enclosing loop
# pass: does nothing at all