# filter: Python’s filter function allows us to return a subset of a sequence for which a certain condition is true.
# filter(function, iterable)b 
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s):
    if s["house"] == "Gryffindor":
        return True
    else:
        return False


def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
# print(gryffindors)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])



#another way
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])