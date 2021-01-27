initial_list = input().split("!")

command = input()

while command != "Go Shopping!":
    command_list = command.split()
    item = command_list[1]
    if command_list[0] == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
    if command_list[0] == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
    if command_list[0] == "Correct":
        if item in initial_list:
            item_index = initial_list.index(item)
            initial_list[item_index] = command_list[2]
    if command_list[0] == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input()

print(', '.join(initial_list))