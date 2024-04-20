#print("mew")
#print("mew")
#print("mew")
"""
i = 3
while i != 0:
    print("meow")
    i = i - 1

"""
"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""

"""
# List
for i in [0, 1, 2]:
    print("meow")
"""
"""
for i in range(3):
    print("meow")

"""
# print("meow\n" * 3, end = "")


#for _ in range(3):
 #   print("meow")
"""
while True:
    n = int(input("Wht's n? "))
    if n < 0:
        continue
    else:
        break;

for _ in range(n):
    print("meow")
"""
"""
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    else:
        continue

for _ in range(n):
    print("meow")
"""
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
def meow(n):
    for _ in range(n):
        print("meow")


"""

"""
def main():
    number = get_number()
    n = meow(number)

def get_number():
    n = int(input("What's x"))
    if n > 0:
        break
    
    return n
        
def meow(n):
    print("meow")
 """   
def main():
    #n = int(input("What's X? "))
    number = get_number()
    n = meow(number)

def get_number():
    
    while True:
        n = int(input("What's x? "))
        if n > 0:
            break
    return n
    #return number



def meow(n):
    for _ in range(n):
        print("meow")

main()











