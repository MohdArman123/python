# name = input("What's your name? ")
# print(f"hello, {name}")

# names =[]
# for _ in range(3):
#     names.append(input("What's your name?" ))

# for name in sorted(names):
#     print(f"hello, {name}")


# sorted(iterable, /, *, key=None, reverse=False)


# name = input("What's your name? ")
# file = open("names2.txt", "a")
# file.write(name)
# file.close()

# name = input("What's your name? ")
# file = open("names2.txt", "a")
# file.write(f"{name}\n")
# file.close()


# name = input("What's your name? ")
# with open("names2.txt", "a")as file:
#     file.write(f"{name}\n")

# with open("names2.txt", "r") as file:
#     lines = file.readlines()
# for line in sorted(lines):
#     print(f"hello, {line.rstrip()}")


# with open("names2.txt", "r") as file:
#     for line in sorted(file):
#         print(f"hello, {line.rstrip()}")
     

# names = []
# with open("names2.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"hello, {name}")


# with open("names2.txt", "r") as file:
#     for line in sorted(file, reverse=True):
#         print("hello, ", line.rstrip())

names = []
with open("names2.txt", "r") as file:
    for line in sorted(file):
        names.append(line.rstrip())

for name in names:
    print(f"hello, {name}")










