balance = 0

def main():
    print("balance", balance)
    deposit(100)
    withdraw(50)
    print("balance" ,balance)


def deposit(n):
    global balance   # global keyword tells each function that balance does not refer to a local variable: instead, it refers to the global variable 
    balance += n               

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

    