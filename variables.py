# # python variable
x = 5
y = "clinton"
print(x)
print(y)

x = str(5)
y = int(5)
z = float(5)
print(x)
print(y)
print(z)


# # variable names
myvar = "clinton"
my_var = "clinton"
_my_var = "clinton"
myVar = "clinton"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)

# assign multiple values
x, y, z = "ram", "shayam", "hari"
print(x)
print(y)
print(z)
# unpack a list
fruits  = ["apple", "banana", "cherry"]
x, y ,z = fruits
print(x)
print(y)
print(z)

# outputvariable
x = "football is love"
print(x)

#
x = "football"
y = "is"
z = "love"
print(x, y, z)

# +character

x = 2
y = 5
print(x+y)

# global variable



x = "love"
def myfunc():
 x = "awesome"
 print("football is " + x)
myfunc()
print("football is " + x)
