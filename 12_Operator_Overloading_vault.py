# class Bank:
#     def __init__(self, rupees=0, dollars=0, rubels=0):
#         self.rupees = rupees
#         self.dollars = dollars
#         self.rubels = rubels

#     def __str__(self):
#         return f"{self.rupees} rupees, {self.dollars} dollars, {self.rubels} rubels"
    



# arman_sal = Bank(100, 50, 25)
# print(arman_sal)
# farhan_sal = Bank(25, 50, 100)
# print(farhan_sal)

# rupees = arman_sal.rupees + farhan_sal.rupees
# dollars = arman_sal.dollars + farhan_sal.dollars
# rubels = arman_sal.rubels + farhan_sal.rubels

# total = Bank(rupees, dollars, rubels)
# print(total)





# operator overloading
class Bank:
    def __init__(self, rupees = 0, dollars = 0, rubel = 0):
        self.rupees = rupees
        self.dollars = dollars
        self.rubel = rubel

    def __str__(self):
        return f"{self.rupees} rupees, {self.dollars} dollars, {self.rubel} rubel"
    
    def __add__(self, other):
        rupees  = self.rupees + other.rupees
        dollars = self.dollars + other.dollars
        rubel = self.rubel + other.rubel
        return Bank(rupees, dollars, rubel)


arman_sal = Bank(100, 50, 25)
print(arman_sal)
farhan_sal = Bank(25, 50, 100)
print(farhan_sal)
total = arman_sal + farhan_sal
print(total)

