"""
students = ["arman", "farhan", "imran"]

#for student in students:
    #print(student)


for i in range(len(students)):
    
    print(i+1, students[i])
"""
"""
students = {
    "arman" : "Delhi",
    "farhan" : "Delhi",
    "imran" : "Delhi",
    "rehan" : "Bihar",
} 
#print(students["arman"])
#print(students["rehan"])
#print(students["imran"])
#print(students["farhan"])

for student in students:
    print(student, students[student], sep = ", ")
"""


students = [
    
    {"name": "arman", "house":"Delhi", "patronus":"otter"},
    {"name":"farhan", "house":"Delhi", "patronus":"stag"},
    {"name":"rehan", "house":"Delhi", "patronus":"jack russell terrier"},
    {"name":"bholu", "house":"noida", "patronus":"None"},
]
for student in students:
    print(student["name"], student["house"],student["patronus"], sep = ", ")














