contests_dict = {}
users_dict = {}

while True:
    command = input()
    if command == "no more time":
        break
    else:
        command_list = command.split(" -> ")
        username = command_list[0]
        contest_name = command_list[1]
        points = int(command_list[2])

        # if username not in users_dict:
        #     users_dict[username] = {}

        if contest_name not in contests_dict:
            contests_dict[contest_name] = {}
        if username not in contests_dict[contest_name]:
            contests_dict[contest_name][username] = points
            # users_dict[username][contest_name] = points
        else:
            if points > contests_dict[contest_name][username]:
                contests_dict[contest_name][username] = points
                # users_dict[username][contest_name] = points

# for (key, value) in users_dict.items():
#     sum_points = 0
#     for (course, points) in value.items():
#         sum_points += points
#         users_dict[key] = points
#
# print(users_dict)

for (key, value) in contests_dict.items():
    count = 1
    print(f"{key}: {len(value)} participants")

    for name, points in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{count}. {name} <::> {points}")
        count += 1

print("Individual standings:")
users_dict = {}
for language in contests_dict:
    for user, points in contests_dict[language].items():
        if user not in users_dict:
            users_dict[user] = 0
            users_dict[user] = points
        else:
            users_dict[user] += points
count = 1
for name, points in sorted(users_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{count}. {name} -> {points}")
    count += 1
