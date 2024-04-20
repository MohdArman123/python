# Classes is like a blueprint or mold which you can define and give a name 
# when you use that mold or bluiprint you get types of data that are designed exactly as you want 

# classes allow you to invent own data type in pythom and give them a name

#classes is a blueprint we use hat bluiprint to build specific object

# class Student:
#     ... 

# def main():
#     student = get_student()
#     print(Student)
#     print(f"{student.name} from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     print(student)
#     return student

# main()


class Student:
    ...

def main():
    stu = get_student()
    print(f"{stu.name} from {stu.house}")


def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student

    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student 


main()



