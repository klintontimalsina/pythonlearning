# num=a and deno=b
class Fraction(object):
    def __init__(self, a, b):

        self.a = a
        self.b = b


    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        num1 = self.a*other.b + self.b*other.a
        den1 = self.b*other.b
        return Fraction(num1,den1)

    def __sub__(self, other):
        num2 = self.a*other.b - self.b*other.a
        den2 = self.b*other .b
        return Fraction(num2,den2)


f1 =Fraction(5, 7)
f2 = Fraction(5, 8)
f3 = f1+f2
f4 = f1-f2
print (f1)
print (f2)
print(f3)
print(f4)





