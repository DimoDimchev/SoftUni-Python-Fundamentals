command = input()

result_dict = {}
language_dict = {}

while command != "exam finished":
    command_list = command.split("-")
    if len(command_list) > 2:
        user = command_list[0]
        language = command_list[1]
        points = int(command_list[2])

        if user not in result_dict:
            result_dict[user] = points
        else:
            if points > result_dict[user]:
                result_dict[user] = points

        if language not in language_dict:
            language_dict[language] = 0

        language_dict[language] += 1
    else:
        result_dict.pop(user)
    command = input()

result_dict = dict(sorted(result_dict.items(), key=lambda x: (-x[1], x[0])))
language_dict = dict(sorted(language_dict.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for (user, points) in result_dict.items():
    print(f"{user} | {points}")
print("Submissions:")
for (language, submissions) in language_dict.items():
    print(f"{language} - {submissions}")
