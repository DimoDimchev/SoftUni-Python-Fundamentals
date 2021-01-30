registered_dict = {}
number_commands = int(input())

for _ in range(number_commands):
    command_list = input().split()
    command = command_list[0]
    username = command_list[1]

    if command == "register":
        license_plate = command_list[2]
        if username not in registered_dict:
            registered_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_dict[username]}")

    if command == "unregister":
        if username not in registered_dict:
            print(f"ERROR: user {username} not found")
        else:
            registered_dict.pop(username)
            print(f"{username} unregistered successfully")

for (key, value) in registered_dict.items():
    print(f"{key} => {value}")