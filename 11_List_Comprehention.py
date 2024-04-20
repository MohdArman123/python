# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = [word.upper() for word in words]
#     print(*uppercased)

# if __name__ == "__main__":
#     main()


 
students = [
    {"name" : "Arman", "House" : "Delhi"},
    {"name" : "Farhan", "House" : "Delhi"},
    {"name" : "Rehan", "House": "Delhi"},
    {"name" : "Imran", "House" : "Delhi"},
    {"name" : "Bholu", "House" : "Bengal"},
]

Delhi = [
    student["name"] for student in students if student["House"] == "Delhi"
]

for delhi in sorted(Delhi):
    print(delhi)