class Computer:
     def config(self):                # self is a object which i have passing
           print("i5, 16gb, 1TB")



com1 = Computer()    # object
com2 = Computer()
     
Computer.config(com1)    # call it with class by passing the object
Computer.config(com2)    
    #or
com1.config()       # # call method config using object itself
com2.config()     # com2 is an object it goes as a parameter




# class Computer:
#     def bit_length(self):
#         print(a)

# a = Computer()
# a=5
# a.bit_length()

# a = 5
# a.bit_length()    # a is an object which is passed as an argument
