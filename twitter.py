# Extracting User Input

# url = input("URL: ").strip()
# print(url)


# url = input("URL: ").strip()
# username = url.replace("https://www.facebook.com/", "")
# username = url.removeprefix("https://www.facebook.com/")
# print(f"Username: {username}")


# import re
# url = input("URL: ").strip()
# username = re.sub(r"https://www.facebook.com/", "", url)
# print(f"Username: {username}") 

# import re
# url = input("URL: ")
# username = re.sub(r"^(https?://)?(www\.)?facebook\.com/", "", url)
# print(f"Username: {username}")



# import re
# url = input("URL: ")
# matches = re.search(r"^https?://(www\.)?facebook\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     # print(f"Username:", matches.group(1))
#     print(f"Username:", matches.group(2))




# import re
# url = input("URL: ")
# if matches := re.search(r"^https?://(?:www\.)?facebook\.com/(.+)$", url, re.IGNORECASE):

#     print(f"Username:", matches.group(1))
#     # print(f"Username:", matches.group(2))


import re
url = input("URL: ")
if matches := re.search(r"^https?://(?:www\.)?facebook\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    
    print(f"Username:", matches.group(1))
    # print(f"Username:", matches.group(2))


