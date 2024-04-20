# with open("students1.csv", "r") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(row)
#         print(f"{row[0]} is in {row[1]}")
        # print(line)
        # print(f" {line[0].rstrip().split(',')} is in {line[1].rstrip().split(',')}")




# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         print(name,home)
#         print(f"{name} is in {home}")


# students = []
# with open("students1.csv") as file:
#     for line in file:
#         students.append(line.rstrip().split(","))
# print(students)
# for name, home in sorted(students):
#     print(f"{name} is in {home}")


# students = []
# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         students.append(f"{name} is in {home}")
# print(students)
# for student in sorted(students):
#     print(student)

        # print(line)
        # name, home = line.rstrip().split(",")
        # students.append(f"{name} is in {home}")
        # students.append(line.rstrip().split(","))
        # row = line.rstrip().split(",")
        # names.append(f"{row[0]} is in {row[1]}")
# print(students)
# for student in sorted(students):
#     print(student)
# for name, home in sorted(students):
#     print(f"{name} is in {home}")
# for row[0], row[1] in names:
#     print(f"{row[0]} is in {row[1]}")
    # print(f"{name} is in {home}")
    # print(student)
    # print(f"{name} is in {home}")



# students = []
# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {}
#         # print(student)
#         student["name"] = name
#         student["home"] = home
#         print(student)
#         students.append(student)
# print(students)
# for student in students:
#     print(f"{student['name']} is in {student['home']}")


# teachers = []
# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.strip().split(",")
#         teacher = {"name" : name, "home" : home}
#         teachers.append(teacher )

# for student in teachers:
#     print(f"{student['name']} is in {student['home']}")


# students = []
# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name":name, "home":home}
#         students.append(student)
# def get_name(student):
#     return student["name"]
# # for student in sorted(students, key = get_name, reverse = True):
# for student in sorted(students, key = get_name):
#     print(f"{student['name']} is in {student['home']}")



# students = []
# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name" : name, "home" : home}
#         students.append(student)
# for student in sorted(students, key = lambda sudent : student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# import csv
# students = []
# with open("students1.csv") as file:
#     reader = csv.reader(file)
#     # print(reader)
#     for row in reader:
#         # print(row)
#         students.append({"name" : row[0], "home" : row[1]})
# print(students)
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")



# import csv
# students = []
# with open("students1.csv") as file:
#     reader = csv.reader(file)
#     # print(reader)
#     for name, home in reader:
#         # print(row)
#         students.append({"name":name, "home":home})
# # print(students)
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# import csv
# students = []
# with open("students1.csv") as file:
#     reader = csv.reader(file)
#     # print(reader)
#     for name, home in reader:
#         students.append({"name":name, "home":home})
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# import csv
# students = []
# with open("students1.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name" : row["name"], "home" : row["home"]})
# for student in sorted(students, key = lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")








