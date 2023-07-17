# use for, .split and if to create a statement that will print out words starts with 's'

st = 'Print only the words that start with s in this sentence'

split_word = st.split()
print(split_word)
for wrd in split_word:
    if wrd[0].lower() == 's':
        print(wrd)

# use range() to print all even numbers from 0 to 10

print(list(range(0, 10, 2)))

#or
for num in range(0, 10):
    if num % 2 == 0:
        print (num)
#or
even_number = [num for num in range(0, 10) if num % 2 == 0]
print(even_number)

# use a list comprhension to create a list of all numbers between 1 and 50 that are divisible by 3

print(list(num for num in range(1, 50) if num % 3 == 0))

# go through the string below and if the length of the word is even print "even"
st = 'print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word + " is even")

#other question
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)