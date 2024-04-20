# meows = 3

# for _ in range(meows):
#     print("meow")

class Cat:
    MEOW = 3

    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow")

cat = Cat()
cat.meow()