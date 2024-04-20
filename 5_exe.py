class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter for name
    @property
    def name(self):
        return self.name
    
    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name   

    # Getter
    @property      #  decorator allows you to define a method that behaves like an attribute.
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Janakpuri", "Janak", "Uttam Nagar", "Dwarka"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
     