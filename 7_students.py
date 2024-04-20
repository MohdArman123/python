class Student:

    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name? ")
        if house not in ["Delhi", "Mumbai", "Kolkata", "Goa", "Up"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):   #str method called automatically and  covert a student object to a string
        return f"{self.name} from {self.house}"



def main():
    student = get_student()
    student.house = "Bihar Patna, Batura"
    print(student)
    # print(student.name, student.house)  # use when don't use str method


def get_student():
    name =  input("Name: ")
    house = input("House: ")
    return Student(name, house)    # Student constructor which invokes automatically __init__ method



if __name__ == "__main__":
    main()
