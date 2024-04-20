# import csv
# students =[]

# with open("students3.csv") as file:
#     reader = csv.reader(file)
#     print(reader)
#     for row in reader:
#         print(row)
#         students.append({"name" : row[0], "home" : row[1]})
# print(students)
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# import csv
# students = []

# with open("students3.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
#         students.append({"name" : row["name"], "house" : row["house"]})
# print(students)
# for student in sorted(students, key = lambda student:student["name"]):
#     print(f"{student['name']} is from {student['house']}")


import csv
students = []
name = input("What's your name? ")
home = input("What's your home? ")

with open("students3.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name" : name, "home" : home})

