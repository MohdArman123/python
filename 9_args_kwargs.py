def f(*args, **kwargs):
    print("Positional: ", args)

f(100, 50, 25)


def f(*args, **kwargs):
    print("Named: ", kwargs)

f(rs=100, dl=50, rb=25)