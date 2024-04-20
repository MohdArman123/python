# Python has an existing library called re that has a number of built-in functions that can validate user inputs against patterns.
# One of the most versatile functions within the library re is search.
# re.search(pattern, string, flags=0)

# import re

# email = input("What's your name? ")
# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid") 

#  regular expressions there are certain symbols that allow us to identify patterns. 
#  A non-exhaustive list of those patterns is as follows:
 
# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions

# email = input("What's your name? ")

# # if re.search(".*@.*", email):
# if re.search(".+@.+", email):
#     print("Valid")
# else:
#     print("Invalid")


# import re
# email = input("What's your email? ").strip()
# if re.search("@", email):
#     print("valid")
# else:
#     print("invalid")



# email = input("What's your mail? ")

# if re.search(".+@.+", email):
#     print("valid")
# else:
#     print("invalid")

# email = input("What your email? ")
# if re.search("..*@..*", email):
#     print("Valid")
# else:
#     print("invalid")

# Placing an r in front of a string tells the Python interpreter to treat the string as a raw string,
# similar to how placing an f in front of a string tells the Python interpreter to treat the string as a format string:

# email = input("What's your email? ")
# if re.search(r".+@.+\.com", email):
#     print("valid")
# else:
#     print("invalid")


# more special symbols at our disposal in validation:

# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string

# email = input("What's your email? ")
# if re.search(r"^.+@.+\.edu$", email):
#     print("valid")
# else:
#     print("invalid")


# []  set of characters
# [^] complementing the set

# email = input("What's your email? ")
# if re.search(r"^[^@]+@[^@]+\.com$", email):
#     print("valid")
# else:
#     print("invalid")

# import re
# email = input("What's your email? ")
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
#       print("valid")
# else:
#      print("invalid")
        
# email = input("What's your email? ")
# if re.search(r"^\w+@\w+\.com$", email):
#     print("valid")
# else:
#     print("invalid")



# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character


# email = input("What's your email? ")
# if re.search(r"^\w+@\w+\.(com|edu|org|net|gov)$", email):
#     print("valid")
# else:
#     print("invalid")

# email = input("What's your email? ")
# if re.search(r"^(\w\s)+@\w+\.(com|edu|org|net|gov)$", email):
#     print("valid")
# else:
#     print("invalid")


# Adding even more symbols to our vocabulary
# A|B     either A or B
# (...)   a group 
# (?:...) non-capturing version


# Case Sensitivity
# Some built-in flag variables are:
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

# import re
# email = input("What's your email? ")
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("invalid")


import re
email = input("What's your email? ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("invalid")