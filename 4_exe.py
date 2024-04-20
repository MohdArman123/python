# class Student:
#     def __init__(self, name, house, favorite_dish):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Delhi", "Mumbai", "Bihar", "Noida", "New Delhi"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.favorite_dish = favorite_dish

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def enjoy_dish(self):
#         match self.favorite_dish:
#             case "Biryani":
#                 return "🍛"
#             case "Paneer Tikka":
#                 return "🍽️"
#             case "Samosa":
#                 return "🥟"
#             case _:
#                 return "🍴"

# def main():
#     student = get_student()
#     print("Enjoy Your Favorite Indian Dish!")
#     print(student.enjoy_dish())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     favorite_dish = input("Favorite Indian Dish: ")

#     return Student(name, house, favorite_dish)

# if __name__ == "__main__":
#     main()




# class Boy:
#     def __init__(self, name, place, favorite_dish):
#         if not name:
#             raise ValueError("Missing name")
#         if place not in ["Janak", "Janakpuri", "Uttam Nagar", "Nehru Place", "District Centre"]:
#             raise ValueError("Wrong Place")
#         self.name = name
#         self.place = place
#         self.fav = favorite_dish

#     def __str__(self):
#         return f"{self.name} goes {self.place} to eat {self.fav}"
    
#     def hotel(self):
#         match self.fav:
#             case "Biryani":
#                 return "Biryani"
#             case "Chikken Tikka":
#                 return "Chikken Tikka"
#             case "Mutton Kurry":
#                 return "Mutton Kurry"
#             case _:
#                 return "Anything!"

# def main():
#     boy = get_boy()
#     print("WAHH WAHH !!")
#     # boy.hotel()
#     print(boy)

# def get_boy():
#     name = input("Name: ")
#     place = input("Place: ")
#     favorite_dish = input("Your Favorite dish: ")
#     return Boy(name, place, favorite_dish)
#     # return boy

# if __name__ == "__main__":
#     main()




























