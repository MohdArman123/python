
#positional arguments
def f(*args, **kwargs):
    print("Positional:", args)   # printed as positional arguments.

f(100, 50, 25)

# named arguments
def f(*args, **kwargs):
    print("Named:", kwargs)

f(rupees=100, dollars=50, rubels=25)



# args and kwargs

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# args are positional arguments, such as those we provide to print like print("Hello", "World").
print("Hello", "World")
# kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="").
print(end="")
