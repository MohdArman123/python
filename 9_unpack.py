# first, _ = input("What's your name? ").split(" ")  # unpack using split
# print(f"hello, {first}")


# def total(rupees, dollars, rubels):
#     return (rupees * 17 + dollars) * 19 + rubels

# print(total(100, 50, 25), "rubels")


def total(rupees, dollars, rubels):
    return (rupees * 17 + dollars) * 19 + rubels

coins = [100, 50, 25]
print(total(coins[0], coins[1], coins[2]), "rubels")


# unpacking the list

def total(rupees, dollars, rubels):
    return (rupees * 17 + dollars) * 19 + rubels
coins = [100, 50, 25]
print(total(*coins), "rubels")  # * used to unpack the list 

 

def total(rupees, dollars, rubels):
    return (rupees * 17 + dollars) * 19 + rubels

print(total(rupees=100, dollars = 50, rubels = 25), "rubels")



def total(rupees, dollars, rubels):
    return (rupees * 17 + dollars) * 19 + rubels

coins = {"rupees" : 100, "dollars" : 50, "rubels" : 25}
print(total(coins['rupees'], coins['dollars'], coins['rubels']), "rubels")

#unpack the dictionary
def total(rupees, dollars, rubels):
    return (rupees * 17 + dollars) * 19 + rubels
coins = {"rupees" : 100, "dollars" : 50, "rubels" : 25}
print(total(**coins), "rubels")   # ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.
# **coins is same as total(rupees=100, dollars = 50, rubels = 25)
 