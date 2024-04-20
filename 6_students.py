class Student:
    def __init__(self, name, house, patronous):

        if not name:
            raise ValueError("Missin name")
        if house not in ["Delhi", "Mumbai", "Bihar", "Noida","New Delhi"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronous = patronous

    def __str__(self):    # str method called automatically anytime when you want to covert a student object to a string
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronous:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🪆"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    # print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")

    return Student(name, house, patronous)



if __name__ == "__main__":
    main()
