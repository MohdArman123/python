# Map: allows to map a function to a sequence of values
# map(function, iterable, ...)

# def main():
#     yell("This is CS50")

# def yell(word):
#     print(word.upper())

# if __name__ == "__main__":
#     main()


# def main():
#     yell(["This", "is", "CS50"])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()



# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)

    print(*uppercased)

if __name__ == "__main__":
    main()