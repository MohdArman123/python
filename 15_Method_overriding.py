# Method Overriding


class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):    # these show override priveous show method
        print("in B Show")

a1 = A()
a1.show()

a1 = B()
a1.show()   # when you call show it will call show method of sub class or child class