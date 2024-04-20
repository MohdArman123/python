# Type Hints
#  Python does not require the explicit declaration of types.
# it’s good practice need to ensure all of your variables are of the right type.
# mypy test is a program that help to ensure all variables are of right type
# in cmd:
#python -m mypy "c:\Users\arman\OneDrive\Desktop\Python_Program\Et Cetera\meows.py"


def meow(n: int) -> None: 
    for _ in range(n):
        print("Meow")


number: int = int(input("Number: ") )   # returns a string,not an int. But meow will likely want an int!
meows: str = meow(number)
print(meows)

