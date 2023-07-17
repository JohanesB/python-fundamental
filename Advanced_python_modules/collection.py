from collections import Counter
my_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 5]
print(Counter(my_list))

wrd = "aaadddddgdgdgd"
cr = Counter(wrd)
print(cr)
print(cr.most_common(2))
print(list(cr))      #list unique elements

lst = ['dsaf', 'sadfd', 111, 1333, 3, 3, 4, 44]
print(Counter(lst[1]))

sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.lower().split()))

from collections import defaultdict #this default dictionary used when there is key error occured which means if there is no key in dictionary it will assign the default value
d = defaultdict(lambda: 0)
d["key1"] = "value1"
print(d["key1"])
print(d["key3"])

from collections import namedtuple
Dog = namedtuple('Dog', ["age", "breed", "name"])
codi = Dog(age=2, breed="husky", name="codi" )
print(codi.breed)