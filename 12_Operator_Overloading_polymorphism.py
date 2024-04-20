# Method Overloading
# operator overloading : whenever you perform any operator like addition sub, division
# behind the scene we are calling a method

# Operator     Magic Method
# +             __add__(self, other)
# -            __sub__(self, other)
# *             __add__(self, other)
# /             __div__(self, other)
# <             __lt__(self, other)
# >             __gt__(self, other)
# >=             __ge__(self, other)
# .                     .
# .                     .
# .                     .
 
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):    # operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
        


s1 = Student(67, 70)
print(s1.m1, s1.m2)
s2 = Student(70, 20)
print(s2.m1, s2.m2)


s3 = s1 + s2    # Student.__add__(s1, s2)

print(s3.m1)