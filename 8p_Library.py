"""
# random.choice(seq)
from random import choice
coin = choice(["heads", "tails"])
print(coin)
"""

"""
# random.randint(a, b)
import random
number = random.randint(1, 10)
print(number)
"""

"""
#random.shuffle(x)
import random
cards = ["Jack", "King", "Queen"]
random.shuffle(cards)
for card in cards:
    print(card)
"""
"""
# Statistics
#average
import statistics

print(statistics.median([100,90,70,60,50,60]))
"""
#command-line arguments
"""
import sys
if len(sys.argv) < 2:
    print("Too Few Arguments")
elif len(sys.argv) > 2:
    print("Too many Arguments")
else:
    print("Hello, my name is", sys.argv[1])

"""
"""
import sys


if len(sys.argv) < 1:
    sys.exit("Too few Arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


"""


# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

 
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

























