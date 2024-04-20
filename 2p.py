

# def hello(to):
#     print("hello,",to)



# name = input("What's your name: ")
# hello(name)
#print(name)


# def hello(to = "World"):
#     print("hello,",to)
# hello()
# name = input("What's your name? ")
# hello(name)



# Scope refers to a variable only existing in which you defined it
# return 
# def main():
#     name = input("What's your name? ")
#     hello(name)
#     hello()
# def hello(to = "world"):
#     print("hello,",to)
# main()



def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    #return n ** 2
    return pow(n,2)
    #return n*n

main()

