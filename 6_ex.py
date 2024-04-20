# import random
# class Village:
#     def __init__(self):
#         self.houses = ["Batura", "Baturi", "Chatar", "Rafiganz"]
    
#     def sort(self, name):
#         # house = random.choice(self.houses)
#         # print(name, "is in", random.choice(self.houses))
#         print(f"{name} is in {self.houses}")


# village  = Village()
# village.sort("Harry") 



import random
class Village:
    houses = ["Batura", "Baturi", "Chatar", "Rafiganz"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
# village = Village()
# village.sort("Arman")

Village.sort("Arman")