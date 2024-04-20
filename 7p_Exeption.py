# Syntax Error
#print("Hello, World)
#print("Hello, World")

# ValueError 
#x = int(input("What's x? "))
#print(f"x is {x}")
"""
#try
try:
    x = int(input("What's x? "))
    print(f"x ix {x}")
except ValueError:
    print("x is not an integer")
"""
"""
#NameError
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x ix {x}")
"""

""" 
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

"""
"""
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
            
    
"""

"""
def main():
    x = get_number("What's x? ")
    print(f"x is {x}")


def get_number(prompt):
    while True:
        try:
             return int(input(prompt))
        except ValueError:
            pass
        

main()

"""
"""     
while True:
    try:
        x = int(input("What's x?"))
        break
    except ValueError:
        print("x is not an integer")
print(f" x is {x}")
"""
"""
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError:
            print("x is not an integer")


main()     
"""
"""
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. 
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError:
            pass
main()

"""
"""
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(user):
    while True:
        try:
            return int(input(user))
        except ValueError:
            pass
main()

"""

  



