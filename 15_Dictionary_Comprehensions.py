"""
students = ["Arman", "Farhan", "Bholu"]

Bihar = []

for student in students:
    Bihar.append({"name": student, "house":"bihar"})

print(Bihar)

"""

# students = ["Arman", "Farhan", "Bholu"]
# Bihar = [{"name" : student, "house": "bihar"} for student in students]
# print(Bihar)



# Dictionary Comprehension
students = ["Arman", "Farhan", "Bholu"]

Bihar = {student : "bihar" for student in students}
print(Bihar)