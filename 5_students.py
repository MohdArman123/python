import sys

class Student:
    def __init__(self, name, house):

        # if name == "":
        if not name:
            raise ValueError("Missing name")
        if house not in ["janakpuri", "Vikaspuri", "palam", "Uttam Nagar", ]:
            raise ValueError("Invalid house")
            # return None
            # sys.exit("Missing name")
            # print("Missing name")
        self.name = name
        self.house = house
        # print(f"{self.name} from {self.house}")

    
    def __str__(self):
        # return "a student"
        return f"{self.name} from {self.house}"



def main():
    student = get_student()
    print(student)
    # print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


    # try:
    #     return Student(name, house)
    # except ValueError:
    #     ...


    # return Student(name, house)



    # student = Student(name, house)
    # print(f"{student.name} from {student.house}")
    # return student



main()