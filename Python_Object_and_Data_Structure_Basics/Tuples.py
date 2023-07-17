# similar to lists but tuples are immutable/ or it can not be reassigned
# tuples uses parenthesis
t = ("one", 2, "three", "four")
print(t)
print(type(t))
t[0] = 1 #error
print(t)