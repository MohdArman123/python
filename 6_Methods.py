# Types of methods
    #1)Instance methods 
        #1) Accessor Methods : for fetch the value
        #2) Mutator Methods : for modify the value
    #2)Class methods 
    #3)Static methods


#1) Instance Method
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):        # Instance Method 
        return (self.m1 + self.m2 + self.m3)/3
    
    def get_m1(self):     # Accessor Method :  fetch the value of instance variable
        return (self.m1)  
    
    def set_m1(self, value):   # mutator Methods : for modify the value of instance variable
        self.m1 = value

s1 = Student(70, 80, 90)
s2 = Student(60, 65, 45)

print(s2.avg())
print(s1.get_m1())
s1.set_m1(30)
print(s1.m1)

# print(s1.m1, s2.m1)

