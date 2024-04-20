#Properties : Attribute
# @property : fuction in python : decorate function 
# decorators : is a function that modify the behaviour of other functions

# class Student:
#     def __init__(self, name, house):

#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Delhi", "Mumbai", "Kolkata", "Goa", "Up"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @property      # Decorator
#     def house(self):
#         return self.house
    
#     @house.setter     #Decorator
#     def house(self, house):
#         if house not in ["Delhi", "Mumbai", "Kolkata", "Goa", "Up"]:
#             raise ValueError("Invalid house")
#         return self.house
        

# def main():
#     student = get_student()
#     student.house = "Dubai"     # Automatically call setter function
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()    


class Student:
    def __init__(self, name, house):                
                self.name = name
                self.house = house

    def __str__(self):
          return f"{self.name} from {self.house}"
    
    @property
    def name(self):
          return self._name
    @name.setter
    def name(self, name):
          if not name:
                raise ValueError("Missing name")
          self._name = name
    @property         # Decorator
    def house(self):
          return self._house
    
    @house.setter      # Decorator
    def house(self, house):
          if house not in ["Delhi", "Mumbai", "UP", "Bihar"]:
                raise ValueError("Invalid 1house")
          self._house = house

def main():
      student = get_student()
      # student.name = ""          
      # student.house = "Dubai
      # student._house = "Dubai"
      print(student)
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
      main()


