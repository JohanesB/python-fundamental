my_list = [1,2,3]
leng = len(my_list)
print(leng)

#concatination
str_list = ["one", "two", "three"]
lst_together = str_list + my_list
print(lst_together)
my_list.append("4")
print(my_list)
print(my_list.count("one"))

#removing items from lists

rem_item_list = lst_together.pop(0)
print(rem_item_list)
print(lst_together)
