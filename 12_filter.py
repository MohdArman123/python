students = [
    {"name" : "Arman", "House" : "Delhi"},
    {"name" : "Farhan", "House" : "Delhi"},
    {"name" : "Rehan", "House": "Delhi"},
    {"name" : "Imran", "House" : "Delhi"},
    {"name" : "Bholu", "House" : "Bengal"},
]

def is_homes(s):
    return s["House"] == "Delhi"

homes = filter(is_homes, students)

for home in sorted(homes, key=lambda s: s["name"]):
    print(home["name"])