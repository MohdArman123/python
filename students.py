 #read comma separated file (csv)
#The split() method is used to split a string into a list of substrings based on a specified delimiter. The delimiter can be a space, a comma, a newline character, or any other character

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(row)
        # print(f"{row[0]} is in {row[1]}")



# with open("students.csv") as file:
#     for line in file:
#         name, house= line.rstrip().split(",") 
#         print(f"{name} is in {house}")


# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # students.append([name, house])
#         students.append(f"{name} is in {house}")

# for student in students:
#     print(student)



# students = []
# with open("students.csv") as file:
#     for line in file:
#         # print(line )
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         # print(student)
#         students.append(student)
# # print(students)
# for student in students:
#     print(f"{student['name']} is in {student['house']}")



# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         # students.append(f"{name} is in {house}")
#         student = {"name" : name, "house" : house}
#         students.append(student)
# def get_house(student):
#     return student["house"]
# for student in sorted(students, key = get_house):
#     print(f"{student['name']} is in {student['house']}")




# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house}
#         students.append(student)
# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is in {student['house']}")



# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name" : name, "home" : house}
#         students.append(student)
# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is in {student['home']}")



# import csv
# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name" : row[0], "home" : row[1]})
# print(students)
# for row in sorted(students, key = lambda student : row[0]):
#     print(f"{row['name']} is from {row['home']}")


# import csv
# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name" : name, "home" : home})
# # print(students)
# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# import csv
# students = []
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name" : row["name"], "home" : row["home"]})
# # print(students)
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# import csv
# name = input("What's your name? ")
# home = input("What's your home? ")

# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])




















