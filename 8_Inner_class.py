# class Student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()   # you can create object of inner class inside the outer class

#     def show(self):
#         print(self.name, self.rollno)
#         self.lap.show()


#     class Laptop():
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i5"
#             self.ram = 8

#         def show(self):
#             print(self.brand, self.cpu, self.ram)


# s1 = Student("Arman", 2)
# s2 = Student("Farhan", 3)

# # print(s1.name, s1.rollno)
# # print(s2.name, s2.rollno)

# s1.show()    #call outer class method  

# s1.lap.show()   # call inner class method

# # print(s1.lap.brand)


# lap1 = Student.Laptop()    # you can create object of inner class outside the outer class provided you use outer class name to call it
# lap1.show()
# # print(lap1.brand)
      




# class Student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()   # you can create object of inner class inside the outer class

#     def show(self):
#         print(self.name, self.rollno)
#         self.lap.show()


#     class Laptop():
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i5"
#             self.ram = 8

#         def show(self):
#             print(self.brand, self.cpu, self.ram)


# s1 = Student("Arman", 2)
# s2 = Student("Farhan", 3)

# # print(s1.name, s1.rollno)
# # print(s2.name, s2.rollno)

# s1.show()    #call outer class method  

# s1.lap.show()   # call inner class method

      









class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        

    def show(self):
        print(self.name, self.rollno)


    class Laptop():
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Arman", 2)
s2 = Student("Farhan", 3)

# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)


lap1 = Student.Laptop()    # you can create object of inner class outside the outer class provided you use outer class name to call it
lap1.show()
# print(lap1.brand)
      
