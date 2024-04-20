# def main():
#      student = get_student()
#      if student[0] == "Arman":
#           student[1] = "Bihar"
#      print(f"{student[0]} from {student[1]}")


# def get_student():
#      name = input("Name: ")
#      house = input("House: ")
#      return [name, house]

# if __name__ == "__main__":
#      main()


# def main():
#     student = get_student()
#     if student["Name"] == "Arman":
#           student["House"] = "Bihar"
#     print(f"{student['Name']} from {student['House']}")

# def get_student():
#         name = input("Name: ")
#         house = input("House: ")
#         return {"Name":name, "House":house}

# if __name__ == "__main__":
#      main()

# class Student:
#     ...
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     s1 = Student()
#     s1.name = input("Name: ")
#     s1.house = input("House: ")
#     print(s1)
#     return s1
# if __name__ == "__main__":
#     main()




# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()


# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#         print(f"{self.name} from {self.house}")


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)
#     # student = Student(name, house)
#     # return student

# if __name__ == "__main__":
#     main()



class Student:

    # def __init__(self, name, house):
    #     self.name = name
    #     self.house = house
    #     print(f"{self.name} from {self.house}")
        
    def config(self, name, house):
        self.name = name
        self.house = house
        print(f"{self.name} from {self.house}")


name = input("Name: ")
house = input("House: ")
student = Student()
student.config(name,  house)


# Encapsulation is one of the main features of Object Oriented Programming (OOP). 
# It refers to the bundling of data and methods that operate on that data within a single unit called a class. 
# The data is encapsulated, or hidden, from outside access, and can only be accessed or modified through the defined methods in the class.

# In the provided example, the Person class encapsulates the data related to a person's name, age, and address. 
# The data is marked as private by using double underscores (__), which means it cannot be directly accessed or modified from outside the class.

# Instead, the class provides getter methods (e.g., get_name(), get_age(), get_address())
#  to access the encapsulated data and setter methods (e.g., set_name(name), set_age(age), set_address(address)) to modify the data in a controlled manner.

# Encapsulation helps to ensure data integrity and provides abstraction by allowing us to hide the internal implementation details of a class. 
# It also allows us to define access restrictions and perform any necessary validation or logic before accessing or modifying the data.


# Certainly! Let's say we have a class called Person which represents a person in our program. 
# We can encapsulate the data related to a person (such as their name, age, and address)
#  and the functions that operate on that data within the Person class.


class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address


# In this example, the data (name, age, and address) is encapsulated within the Person class, and their visibility is restricted using double underscores (__). 
# This makes them private variables, which cannot be accessed or modified directly from outside the class.

# Instead, we provide "getter" (e.g. get_name()) and "setter" (e.g. set_name(name)) methods to access or modify the private data in a controlled manner.
#  These methods allow us to control how the data is accessed and modified, implement any necessary validation or logic, and ensure data integrity.


# Here's an example of how we can create a Person object and use the getter and setter methods:
# Creating a Person object
person = Person("John Doe", 25, "123 Main St")

# Accessing the encapsulated data using getter methods
print(person.get_name())    # Output: John Doe
print(person.get_age())     # Output: 25
print(person.get_address()) # Output: 123 Main St

# Modifying the encapsulated data using setter methods
person.set_name("Jane Doe")
person.set_age(30)
person.set_address("456 Broad Ave")

# Accessing the modified data using getter methods
print(person.get_name())    # Output: Jane Doe
print(person.get_age())     # Output: 30
print(person.get_address()) # Output: 456 Broad Ave








