# use a key-value pair
# use curly braces and colons to map key and value
# objects retrieved by key name
# unordered and can not be sorted

my_dict = {"key1":"value1", "key2":"value2"}
print(my_dict)

prices = {"apples": 3.4 , "banana": 43.4, "orange": 2}
print(prices["apples"])
d = {"k1": 384, "k2": [23,4,3,"jnfd"], "k3": {"insidek3": 203}}
print(d)
print(d["k2"][2])
print(d["k3"]["insidek3"])
print(d.keys())
print(d.values())
print(d.items())