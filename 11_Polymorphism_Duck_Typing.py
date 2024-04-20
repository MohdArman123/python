# Polymorphism : Many forms or one thig will bahave different way

#1) Duck Typing
#2) Operator Overloading
#3) Method Ovrloading
#2) Method Overriding

#1) Duck Typing


# class Vscode:

#     def execute(self):
#         print("Compiling")
#         print("Running")

# class MyEditor:

#     def execute(self):
#         print("Spell Check")
#         print("Convention Check")
#         print("Compiling")
#         print("Running")


# class Laptop:

#     def code(self, ide):
#         ide.execute()  

# # ide = Vscode() 
# ide = MyEditor()

# lap1 = Laptop()
# lap1 .code(ide)






class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)