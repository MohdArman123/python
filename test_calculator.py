# Python’s assert command allows us to tell the compiler that something, some assertion, is true.
# pytest is a third-party library that allows you to unit test your program. That is, you can test your functions within your program.





# test_calculator.py
import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_nagative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")






# from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-3) == 9
#     assert square(-2) == 4
#     assert square(0) == 0

################################################

# from calculator import square

# def main():
#     test_square()

# def test_square():
#     if square(2) != 4:
#         print("2 square is not 4")
#     if square(3) != 9:
#         print("3 square is not 9")
# if __name__ == "__main__":
#     main()


########################################


# from calculator import square
# def main():
#     test_square()

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9

# if __name__ == "__main__":
#     main()


################################################



# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9") 
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9 
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("o squared was not 0")

# if __name__ == "__main__":
#     main()




    