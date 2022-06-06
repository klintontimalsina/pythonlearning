# sort  the list descending
list = [100, 50, 65, 82, 23]
list.sort(reverse = True)
print(list)


# case insensitive

list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort(key = str.lower)
print(list)

# copy()

list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

# join two list

list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# append list2 into list1
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# tuple
tuple = ("apple", "banana", "cherry")
print(tuple[-1])

# return the third,fourth and fifth item
tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[2:5])

# range of negative indexes
tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[-4:-1]
#
