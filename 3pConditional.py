"""
x = int(input("What's x? "))
y = int(input("What's y? "))
if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")


score = int(input("Score: "))
if score >= 90 and score <=100:
    printf("Grade A")
elif score >= 80 and score <= 90:
    print("Grade B")
elif score <= 70 and score <= 80:
    print("Grade C")
elif score <= 60 and score <= 80:
    print("Grade D")
else:
    print("Grade E")
 

score = int(input("Score: "))
if score >= 90:
    print("Grade A")
elif score>= 80:
    print("Grade B")
elif score >=70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade E")
"""

"""
x = int(input("What's x? "))
if x %2 ==0:
    printf("Even")
else:
    print("Odd")
"""

"""
# Creating Our Own Parity Function


def main():
    x = int(input("Whaty's x? "))
    if is_even(x):
        print("Even")
    else:
        printf("Odd")
def is_even(n):

    if n % 2 == 0:
        return True
    else:
        return False
main()

"""

"""
def main():
    x = int(input("Whaty's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return True if n % 2 == 0 else False
main()
"""

"""
def main():
    x = int(input("Whaty's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return n % 2 == 0
main()

"""

# match 
"""
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Arman")

elif name == "Draco":
    print("Farhan")

else:
    print("Who?")

"""

"""
name = input("What's your name? ")

match name:
    case "Arman":
        print("Bad")
    case "Farhan":
        print("Bad")
    case "Imran":
        print("Bad")
    case "Rehan":
        print("Good")
    case "Bholu":
        print("Very Good")
    case _:
        print("Who?")
"""

name = input("What's your name? ")
match name:
    case "Arman" | "Farhan" | "Imran":
        print("Bad")
    case "Rehan":
        print("Good")
    case "Bholu":
        print("Very Good")
    case _:
        print("Who?")







































































