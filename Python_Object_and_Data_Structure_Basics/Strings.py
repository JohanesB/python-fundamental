word = "hello world"
print(word)
print(len(word))

#string indexing and slicing
print(word[0]) #indexing
print(word[-1]) #reverse indexing

print(word[2:]) #starting from index 2
print(word[:5]) #print upto index 5, but 5 is exclude
print(word[2:9]) #print from index 2 upto 9, but 9 is excluded
print(word[::2]) #jumping step size of 2

name = "yohanes"
x = name[1:]
name = "J" + x
print(name)
mul = name * 10 #string multiplication
print(mul)

#string formating for printing

print("Today is {}".format("a special daty"))
print("the {} {} {}".format("fox", "brown", "quick"))
print("the {2} {1} {0}".format("fox", "brown", "quick"))
print("the {q} {f} {b}".format(f="fox", b="brown", q="quick"))

result = 33434/435
print("the result is {r:1.4f}".format(r=result)) #float formatting

studentName = "yohanes";
age = "23"
print(f"the student name is {studentName} and his age is {age}") #f string literals