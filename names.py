# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))
#     # names.append(name)


# for name in sorted(names):
#     print(f"hello, {name}")


# File I/O allows your program to store this information such that it can be used later. 

# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# The keyword with allows you to automate the closing of a file.
# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# name = input("What's your name? ")
# print(f"hello, {name}")


# names = []
# for _ in range(3):
#     name = input("What's your name ?")
#     names.append(name)
# for name in sorted(names):
#     print(f"hello, {name}")



# name = input("What's your name ?")

# file = open("names1.txt", "a")
# file.write(f"{name}\n") 
# file.close()


# name = input("What's your name? ")

# with open("names1.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names1.txt", "r") as file:
#     lines = file.readlines()    #readlines has a special ability to read all the lines of a file and store them in a file called lines. 
    

# for line in lines:
#     print("hello,", line.rstrip())                

#Notes
#rstrip(): This method removes only the trailing whitespace (including spaces, tabs, and line breaks) from the right end of the string. It doesn't affect the leading whitespace or characters in the middle of the string.
#strip(): This method removes both leading and trailing whißtespace from the string. It removes spaces, tabs, and line breaks from both ends of the string.
#splitlines() method is used to split the text into lines, and then join() is used to combine the lines back together with newlines, effectively removing any trailing whitespace, including line breaks.
# print("hello, ",'\n' .join(line))

# names = []
# with open("names1.txt", "r") as file:
#     for name in file:
#         # print(name)
#         names.append(name.rstrip())
# # print(names)
        
# for line in sorted(names):
#     print("hello, ", line)

# names = []
# file = open("names1.txt", "r")
# for line in file:
#     names.append(line.rstrip())
# for name in sorted(names):
#     print(f"hello", name)


# with open("names.txt", "r") as file:
#     for line in sorted(file):
#         print("hello, ", line.strip())


with open("names.txt", "r") as file:
    for line in sorted(file, reverse = True):
        print("hello, ", line.strip())



 





