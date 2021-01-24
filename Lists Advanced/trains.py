number_of_wagons = int(input())

wagons_list = [0 for _ in range(number_of_wagons)]

command = input()

while command != "End":
    command_list = command.split()

    if command_list[0] == "add":
        wagons_list[len(wagons_list)-1] += int(command_list[1])
    elif command_list[0] == "insert":
        wagons_list[int(command_list[1])] += int(command_list[2])
    elif command_list[0] == "leave":
        wagons_list[int(command_list[1])] -= int(command_list[2])

    command = input()

print(wagons_list)