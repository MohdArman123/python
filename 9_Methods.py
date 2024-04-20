

# print(type(50))
# print(type("Arman"))
# print(type([]))
# print(type(list()))
# print(type({}))
# print(type(dict()))


# Instace Method
import random
class Hat:

    def __init__(self):
        self.houses = ["Batura", "Baturi", "Gaya", "Aurangabad"]  # Instance variable

    def sort(self, name):       # instance method
        # house = random.choice(self.houses)
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")


# Class Method
# import random
# class Hat:
#     houses = ["Batura", "Baturi", "Gaya", "Aurangabad"]    #class variables     

#     @classmethod       # Decorator
#     def sort(cls, name):            # class method
#         print(name, "is in", random.choice(cls.houses))

# Hat.sort("Arman")