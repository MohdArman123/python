# Type Hints
# Python does not require the explicit declaration of types.
# it’s good practice need to ensure all of your variables are of the right type.
# mypy test is a program that help to ensure all variables are of right type
# in cmd:
# python -m mypy "c:\Users\arman\OneDrive\Desktop\Python_Program\Et Cetera\5_type_hint_meow.py"  

def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number"))

meows: str = meow(number)
print(meows, end="")


# def meow(n : int):
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meow(number)



# def meow(n : int) -> str:
#     # for _ in range(n):
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)












