# Cleaning Up User Input

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")



# import re 
# name = input("What;s your name? ")
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"hello, {name}")


# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last = matches.group(1)
#     first = matches.group(2)
#     name = f"{first} {last}"
# print(f"hello, {name}")



# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last = matches.group(1)
#     first = matches.group(2)
#     name = f"{first} {last}"
# print(f"hello, {name}")


# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")



# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")



# The walrus := operator assigns a value from right to left and allows us to ask a boolean question at the same time.
import re
name = input("What's your name? ")
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")






name = input("What's your name? ")
# matches = re.search(r"^(.+), (.+)$", name)
# matches = re.search(r"^(.+), ?(.+)$", name)
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
    # last = matches.group(1)
    # first = matches.group(2)
    # last, first = matches.groups()
    # name = f"{first} {last}"
print(f"hello, {name}")


