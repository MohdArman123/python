"""
print("#")
print("#")
print("#")
"""
"""
for _ in range(3):
    print("#")
"""
"""
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
"""
"""
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end = "")
main()

"""
"""
for _ in [0,1,2,3]:
    print("?", end = "")


for _ in range(4):
    print("?", end = "")

for _ in range(4):
    print("?", end = "")

"""

"""
def main():
    print_row(4)

def print_row(width):
    for _ in range(width):
        
        print("?", end = "")

main()
"""
"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
"""
"""
def main():
    print_square(3)


def print_square(size):
    
    for _ in range(size):

        for j in range(size):
            
            print("#", end = "")
        print()


main()
"""
"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)
main()

"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_width(size)

def print_width(size):
    print("#" * size)
main()















    

























































    
