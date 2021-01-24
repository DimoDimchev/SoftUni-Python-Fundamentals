# creates a list with all targets
targets = [int(element) for element in (input().split())]

command = input()
command_list = []

# a loop that changes the list, depending on the given command
while command != "End":
    command_list = command.split()
    command_index = int(command_list[1])
    if "Shoot" in command:
        if 0 <= command_index < len(targets):
            targets[command_index] -= int(command_list[2])
            if targets[command_index] <= 0:
                targets.remove(targets[command_index])
    elif "Add" in command:
        if 0 <= command_index < len(targets):
            targets.insert(command_index, int(command_list[2]))
        else:
            print("Invalid placement!")
    elif "Strike" in command:
        radius = int(command_list[2])
        left_index = command_index - radius
        right_index = command_index + radius

        if left_index >= 0 and right_index < len(targets):
            left_part = targets[:left_index]
            right_part = targets[right_index+1:]
            targets = left_part + right_part
        else:
            print("Strike missed!")

    command = input()

# prints the remaining targets
for i in range(len(targets)-1):
    print(targets[i], end="|")
print(targets[len(targets)-1])