usernames_list = input().split(", ")
valid_list = []

for username in usernames_list:
    if 3 < len(username) < 16:
        username_check = ""
        for char in username:
            if char.isalpha() or char.isdigit() or char == "-" or char == "_":
                username_check += char
        if username == username_check:
            valid_list.append(username)

for username in valid_list:
    print(username)