dwarves_dict = {}
colors_dict = {}

while True:
    command = input()
    if command == "Once upon a time":
        break
    else:
        command_list = command.split(" <:> ")
        name = command_list[0]
        color = command_list[1]
        physics = int(command_list[2])

        dwarf = name + ":" + color
        if dwarf not in dwarves_dict:
            if color not in colors_dict:
                colors_dict[color] = 1
            else:
                colors_dict[color] += 1
            dwarves_dict[dwarf] = [0, color]
        dwarves_dict[dwarf][0] = max(physics, dwarves_dict[dwarf][0])

sorted_dwarves = sorted(dwarves_dict.items(), key=lambda x: (-x[1][0], -colors_dict[x[1][1]]))
for (key, value) in sorted_dwarves:
    current = key.split(":")
    print(f"({current[1]}) {current[0]} <-> {value[0]}")
