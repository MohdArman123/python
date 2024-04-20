class Student:
    def __init__(self, name, house):    # Instance mathod  : Initialize the content of an object from a class when define these method
        self.name = name                # instance variable
        self.house = house
         

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)   # constructor call
    return student

main()
