# first, _ = input("What's your Name? ").split(" ")
# print(f"hello, {first}")

# def total(rs, dl, rb):
#     return (rs * 17 + dl) * 29 + rb
# print(total(100, 50, 25))


# def total(rs, dl, rb):
#     return (rs * 17 + dl) * 29 + rb
# coins = [100, 50, 25]
# print(total(coins[0], coins[1], coins[2]), "rb")


# def total(rs, dl, rb):
#     return (rs * 17 + dl) * 29 + rb
# coins = [100, 50, 25]
# print(total(*coins), "rb")


# def total(rs, dl, rb):
#     return (rs * 17 + dl) * 29 + rb
# print(total(rs=100, dl=50, rb = 25), "rb")



# def total(rs, dl, rb):
#     return (rs * 17 + dl) * 29 + rb
# coins = {"rs":100, "dl":50, "rb":25}
# print(total(coins["rs"], coins["dl"], coins["rb"]), "rb")



def total(rs, dl, rb):
    return (rs * 17 + dl) * 29 + rb
coins = {"rs":100, "dl":50, "rb":25}
print(total(**coins), "rb")