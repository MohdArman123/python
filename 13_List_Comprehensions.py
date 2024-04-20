# List Comprehensions allow you to create a list on the fly in one elegent one-liner

# def main():
#     yell("This", "Is", "Me")


# def yell(*words):
#     uppercased = [word.upper() for word in words]
#     print(*uppercased)

# if __name__ == "__main__":
#     main()



students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student ["house"] == "Gryffindor"
]

print(gryffindors)
for gryffindor in sorted(gryffindors):
    print(gryffindor)