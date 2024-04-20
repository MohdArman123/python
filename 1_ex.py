class Student:
    def __init__(self, name, age, height):
        self.name = name  # public
        self._age = age    # protected
        self.__height = height  # private

s1 = Student("Arman", 24, 6)

print(s1.name)      # public: can be accessed
print(s1._age)       # protected: can be accessed but not advised
# print(s1.__height)    # private: will give AttributeError



