# def add(num1, num2):
#     print(num1 + num2)
# number1 = 10
# number2 = input("please provide a number: ")


try:
    result = 10 + 10
except:
    print("hey, it's look like you aren't adding a number correctly")
else:
    print("add went well!!")
    print(result)

try:
    file = open("testfile", 'r')
    file.write("write a test file")
except TypeError:
    print("there was a type error")
except OSError:
    print("there was an OSError")
finally:
    print("i'm always run")


def ask_for_int():
    while True:
        try:
            result = int(input("please provide a number: "))
        except:
            print("oops, That is not a number")
            continue
        else:
            print("Thank You")
            break
        finally:
            print("end of try/except/finally")
ask_for_int()