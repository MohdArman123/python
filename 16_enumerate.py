students = ["Arman", "Farhan", "Bholu"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])



# enumerate
#enumerate(iterable, start=0)
for i, student in enumerate(students):
    print(i+1, student)