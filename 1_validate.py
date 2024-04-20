# email = input("What's your email? ").strip()
# if "@" in email and "." in email:
#     print("validate")
# else:
#     print("Invalidate")



# email = input("What's your name? ")
# username, domain = email.split("@")
# if username and "." in domain:
#     print("valid")
# else:
#     print("invalid")

# email = input("What's your email? ").strip()
# username, domain = email.split("@")
# if username and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")






# Revision
email = input("What's your email? ").strip()
# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invalid")


# username, domain = email.split("@")
# if username and "." in domain:
#     print("valid")
# else:
#     print("invalid")


username, domain = email.split("@")
if username and domain.endswith(".com"):
    print("valid")
else:
    print("invalid")