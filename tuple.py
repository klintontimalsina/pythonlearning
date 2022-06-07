# new tuple and add tuple
tuple = ("car", "bike", "plane")
y = ("car",)
tuple += y

print(tuple)


# tuple into a list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)