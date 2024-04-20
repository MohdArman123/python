# Inheritance

#1) Single Inheritance
# class A:
#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")


# class B(A):
#     def feature3(self):
#         print("feature 3 working")

#     def feature4(self):
#         print("feature 4 working")

# a1 = A()
# a1.feature1()
# a1.feature2()

# b1 = B()
# b1.feature1()
# b1.feature3()



#2) Multilevel Inheritance

class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class B(A):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(B):
    def feature5(self):
        print("feature 5 working")

    def feature6(self):
        print("feature 6 working")



# a1 = A()
# a1.feature1()
# a1.feature2()

# b1 = B()
# b1.feature1()
# b1.feature3()

# c1 = C()
# c1.feature1()
# c1.feature5()



#3) Multiple Inheritance
class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class B:
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):
    def feature5(self):
        print("feature 5 working")

    def feature6(self):
        print("feature 6 working")



# a1 = A()
# a1.feature1()
# a1.feature2()

b1 = B()
b1.feature1()    # Error: AttributeError: 'B' object has no attribute 'feature1'. Did you mean: 'feature3'    
# b1.feature3()

# c1 = C()
# c1.feature1()
# c1.feature3()
# c1.feature5()
