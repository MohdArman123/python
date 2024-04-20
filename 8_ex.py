class Grandfather:
    def __init__(self, name):
        self.name = name
        print(f"child Granfather name: {self.name}")
        # print("Arman")

class Parent(Grandfather):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        # print(f"Parent Grandfather Name {self.name}")
        # print(f"Parent house: {self.house}")

class Child(Grandfather):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        # print(f"child Granfather name: {self.name}")
        print(f"Child house: {self.subject}")



grandfather = Grandfather("Muslim Miyan")
parent = Parent("Ilyas", "Delhi")
child = Child("Arman", "English")

# child = Child("Delhi")





