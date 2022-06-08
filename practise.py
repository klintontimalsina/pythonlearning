s = {3.14, "sparta", 1 , False}
s.add("hello")
print(s)


s1 = {1, "a", True, 2, "b", False}
s1.update([10 ,20, "hello "])
print(s1)

s1 = {1, "a", True, 2, "b", False}
s1.remove("a")
print(s1)


s1 = {2, 3, 4, 5, 6}
s2 = {3, 4, 5, 2, 7}
print(s1.union(s2))


tup1 = ('a', 'b','c')
if 'd' in tup1:
    print("value a is present in tup1")
else:
    print("value d is not present in tup1")

    a = 10
    print(a)

print(type(a))

a=45
b=60
print(a==b)

a = True
b = False
print(a | b)

student = "ram"
Student = "Ram"
print(student)
print(Student)

my_string = "my name is ujwol"
print(my_string[0])
print(my_string[-3])
print(my_string[2:7])
print(len(my_string))
print(my_string.lower())
print(my_string.upper())
print(my_string.replace('a', 'b'))
print(my_string.count("m"))
print(my_string.find("n"))
print(my_string.split('m'))
