class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("rajat", 56)

print(p1.name)
print(p1.age)

##constructor function

class Complex:
    def __init__(self, realpart, imagpart):
        self.realpart = realpart
        self.imagpart = imagpart
x =Complex(9,-8)
print(x.realpart)
print(x.imagpart)


##
class rectangle:
    def __init__(self, length, breadth):

        self.lenght = length
        self.breadth = breadth

    def rectangle(self):
        return self.length * self.breadth
s1 = rectangle(2, 4)
print(s1.rectangle())


