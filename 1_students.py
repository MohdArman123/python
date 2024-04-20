# this program follows a procedural, step-by-step paradigm: 


# name = input("Name: ")
# house = input("House: ")
# print(f"{name} is from {house}")



# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     name = input("Name: ")
#     return name
# def get_house():
#     house = input("House: ")
#     return house
# if __name__ == "__main__":
#     main()


# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")
# def get_house(): 
#     return input("House: ")
# if __name__ == "__main__":
#     # print(__name__)
#     main()




def main():
    student = get_student()
    if student["name"] == "Arman":
        student["house"] = "rohini"
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    # name = input("Name: ")
    # house = input("House: ")
    # return {"name" : name, "house" : house}

if __name__ == "__main__":
    main()










