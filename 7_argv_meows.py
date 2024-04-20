# python -u "c:\Users\arman\OneDrive\Desktop\Python_Program\Et Cetera\7_argv_meows.py" -n 3

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("Usage: 7_argv_meows.py")