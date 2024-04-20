# map allows to map a function to a sequence of values
# map(function, iterable, ...)


def main():
    yell("This", "Is", "Me")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
if __name__ == "__main__":
    main()



#  map takes two arguments. 
# First, it takes a function we want applied to every element of a list. 
# Second, it takes that list itself, 
# to which we’ll apply the aforementioned function. 


#  Hence, all words in words will be handed to the str.upper function 
#  and returned to uppercased .