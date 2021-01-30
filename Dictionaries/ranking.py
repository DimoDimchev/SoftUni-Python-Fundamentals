import sys

# dictionary that stores all of the contests
contest_dict = {}

# dictionary that stores all of the users
users_dict = {}

# variable to keep track of the highest score
max_score = -sys.maxsize

# loop that receives all the contests and puts them in a dictionary
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        command_list = command.split(":")
        contest = command_list[0]
        password = command_list[1]
        contest_dict[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    else:
        command_list = command.split("=>")
        contest = command_list[0]
        password = command_list[1]
        user = command_list[2]
        points = int(command_list[3])

        if contest in contest_dict and password == contest_dict[contest]:
            if user not in users_dict:
                users_dict[user] = {}
            if contest not in users_dict[user]:
                users_dict[user][contest] = points
            else:
                if points > users_dict[user][contest]:
                    users_dict[user][contest] = points

highest_score = ""
for user in users_dict:
    total  = 0
    for course in users_dict[user]:
        total += users_dict[user][course]
    if total > max_score:
        max_score = total
        highest_score = user
print(f"Best candidate is {highest_score} with total {max_score} points.")
print("Ranking:")
for user in sorted(users_dict):
    print(f"{user}")
    for contest, points in sorted(users_dict[user].items(),key=lambda x:-x[1]):
        print(f"#  {contest} -> {points}")

