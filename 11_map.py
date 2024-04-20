# def main():
#     yell("This is me")

# def yell(word):
#     print(word.upper())

# if __name__ == "__main__":
#     main()

# def main():
#     yell(["This", "is", "Me"])

# def yell(words):
#     for word in words:
#         print(word.upper(), end = " ")

# if __name__ == "__main__":
#     main()  


# def main():
#     yell(["This", "is", "Me"])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)   

# if __name__ == "__main__":
#     main()



def main():
    yell("This", "Is", "Me")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()



