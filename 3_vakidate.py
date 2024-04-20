#  regular expressions there are certain symbols that allow us to identify patterns. 
#  A non-exhaustive list of those patterns is as follows:
# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions

# more special symbols at our disposal in validation:
# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string

# []  set of characters
# [^] complementing the set

# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character

# Adding even more symbols to our vocabulary
# A|B     either A or B
# (...)   a group 
# (?:...) non-capturing version


# Case Sensitivity
# Some built-in flag variables are:
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

import re
email = input("What's your email? ").strip()

# if re.search("@", email):
# if re.search("..*@..*", email):
# if re.serch(".+@.+", email):
# if re.search("r.+@.+\.edu", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0_9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email)
# if re.search(r"^\w+@(\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^(\w+|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid") 