# Every time you create an object it is allocated to new space in heap memory

# class Computer:
#     ...

# c1 = Computer()
# c2 = Computer()

# print(id(c1))
# print(id(c2))

#constructor
# Size of an object? : Depends on the no. of variable and size of each variable
# Who allocated size to object? : Constructor Allocated size to object 

# class Computer:
#     def __init__(self):
#         self.name = "Arman"
#         self.age = 22

# c1 = Computer()
# c1.name = "Farhan"
# c1.age = 17
# print("Name : ", c1.name)
# print("Age : ", c1.age)

# c2 = Computer()
# print("Name : ",c2.name)
# print("Age : ", c2.age)



"""
# talk about self:
class Computer:
    def __init__(self):
        self.name = "Arman"
        self.age = 22
    
    def update(self):
        self.age =30


c1 = Computer()
c2 = Computer()


c1.name = "Farhan"
c1.age = 17

c1.update()

print(c1.name)   # Farhan
print(c1.age)    # 30
print(c2.name)   # Arman
print(c2.age)    # 22

"""


# Comparing Object
class Computer:
    def __init__(self):
        self.name = "Arman"
        self.age = 22

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
# c1.age = 17
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("Tehy are different")