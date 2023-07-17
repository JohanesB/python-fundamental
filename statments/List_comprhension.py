word = "yohanes"
list1 = []
for letter in word:
    list1.append(letter)
print(list1)

#using list comprhension 

list2 = [letter for letter in word]
print(list2)

#or

list3 = [x for x in "hello"]
print(list3)

#or

list4 = [num**2 for num in range(0,34)]
print(list4)

#or

list5 = [xn for xn in range(0, 20) if xn % 2 == 0]
print(list5)

#or

celcius = [0, 10, 42, 46, 12.5]
fahrenite = [((9/5)*temp + 32) for temp in celcius]
print(fahrenite)

#using for loop the above question

fahrenite = []
for temp in celcius:
    fahrenite.append((9/5)*temp + 32)
print(fahrenite)
