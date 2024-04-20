# @classmethodi
# we can call this method without instantiating a student object
# i want to able to call get without having a student object
 
# return cls(name, house )
#we can now instantiate a student object by using CLS that passed in
# it just means create an object of the current class that class is whatever cls is


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    

#The get class method is defined within the Student class. 
# This class method takes user input for the name and house, 
# and then it creates and returns a Student object using cls(name, house).
    @classmethod
    def get(cls):              # cls refers to the class itself.
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)    


# cls(name, house) creates a new instance of the Student class with two arguments: name and house. These arguments are passed to the class constructor,
#  which is typically defined in the __init__ method of the class.


def main():
    student = Student.get()  # you call the Student.get() class method to obtain a Student object and store it in the student variable:
    print(student)           # This will call the __str__ method of the Student class, which returns a formatted string representing the student's name and house.

if __name__ == "__main__":
    main()



