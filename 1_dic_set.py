students = [
    {"name" : "Arman", "House" : "Delhi"},
    {"name" : "Farhan", "House" : "Bihar"},
    {"Name" : "Rehan", "House": "UP"},
    {"Name" : "Imran", "House" : "Goa"},
    {"Name" : "Bholu", "House" : "Bengal"},
]

houses = []
for student in students:
    if student["House"] not in houses:
        houses.append(student["House"])
for house in sorted(houses):
    print(house)


# houses = set()
# for student in students:
#     houses.add(student["House"])

# for house in sorted(houses):
#     print(house)