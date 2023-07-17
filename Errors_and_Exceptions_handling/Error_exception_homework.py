for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except:
        print("an error occured")


x = 5
y = 0
try:
    z = x/y
except:
    print("the dnominator must be different from zero")
finally:
    print("All Done")

def Ask():
    while True:
        try:
            result = int(input("please provide a number: \n"))
            square = result ** 2
        except:
            print("An error occurred! please try again!")
            continue
        else:
            print(f"Thank you, your number squared is: {square}")
            break
Ask()