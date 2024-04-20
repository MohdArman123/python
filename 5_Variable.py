#varaible
    #1) instance variable
    #2) class variable

#namespace:
    #1) class namespace : where you will store all the class variable
    #2) object/instance namespace : where you create all the instance variable

class Car:

    wheel = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 20
# c1.wheel = 5
Car.wheel = 5

print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, Car.wheel)

