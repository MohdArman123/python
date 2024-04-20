# method overloading
# operator overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
        

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
    

s1 = Student(50, 25)
s2 = Student(70, 20)


if s1 > s2:
    print("s1 wins")

else:
    print("s2 wins")



a = 9
print(a)    # 9
print(a.__str__())   #  9


print(s1)
print(s1.__str__())
print(s2)   # s2.__str__()