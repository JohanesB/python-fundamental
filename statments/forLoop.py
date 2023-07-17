mylist = [1,2,3,4,5,6,7,8,9]

for num in mylist:
    print(num)
#print even number in the list
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"odd number: {num}")
#add the item in the list

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print("the sum in the list is {}".format(list_sum))

#tuple and packing

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for tup in mylist:
    print(tup)

#tuple and unpacking
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (a, b) in mylist:
    print(a)
    print(b)

#accessing a dictionaries 
dict = {"k1": 1, "k2": 2, "k3": 3}
for key, value in dict.items():
    print(value)
