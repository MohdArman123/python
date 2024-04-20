# Encapsulaion : in OOPs Encapsulation refers to the process which encapsulate all the functionality of a class within the class definetion
#  Bundling or wrapping the data and methods wihin a single unit 
# the data is Encapsulated or hiding from outside access and only be accesed whitin the class

# raise
# class Student:
#     def __init__(self, name, house):
#         if name == "":
#             raise ValueError("Missing name")
#         if house not in ["Delhi", "Bihar", "Mumbai", "UP", "Punjab"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)



class Student:
    def __init__(self, name, house, city):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Delhi", "Up", "Bihar", "Haryana"]:
            raise ValueError("Invalid House")
        if city not in ["west Delhi", "Patna", "Noida", "New Delhi", "Gurgaon"]:
            raise ValueError("Invalid City")
        self.name = name
        self.house = house
        self.city = city
        print(f"{self.name} coming {self.house}")

    def __str__(self):
        return f"{self.name} from {self.house} and {self.city}"

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)


def get_student():

    name = input("Name: ")
    house = input("House: ")
    city = input("City: ")
    student = Student(name, house, city)
    return student

if __name__ == "__main__":
    main()

# name = input("Name: ")
# house = input("House: ")
# student = Student(name, house)
# print(student)
