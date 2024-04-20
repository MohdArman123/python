# argparse : Argument parser to parse or read or analyse
# is a library that handles all the parsing of complicated strings of command-line arguments. In the text editor window, 
# python -u "c:\Users\arman\OneDrive\Desktop\Python_Program\Et Cetera\8_argparse_meows.py" -n 3
import argparse

# An object called parser is created from an ArgumentParser class
parser = argparse.ArgumentParser(description = "Meow like a Cat") 
# add_argument method is used to tell argparse what arguments we should expect from the user when they run our program. 
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# parse_args method ensures that all of the arguments have been included properly by the user.
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
