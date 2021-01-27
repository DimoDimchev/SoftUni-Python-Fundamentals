inventory = input().split(", ")

command = input()

while command != "Craft!":
    command_list = command.split(" - ")
    item = command_list[1]

    if "Collect" in command_list:
        if item not in inventory:
            inventory.append(item)
    elif "Drop" in command_list:
        if item in inventory:
            inventory.remove(item)
    elif "Combine Items" in command_list:
        old_item = item.split(":")[0]
        second_item = item.split(":")[1]
        if old_item in inventory:
            inventory.insert((inventory.index(old_item)) + 1, second_item)
    elif "Renew" in command_list:
        if item in inventory:
            copied_item = item
            inventory.remove(item)
            inventory.append(copied_item)

    command = input()

for i in range(len(inventory)-1):
    print(inventory[i], end=", ")
print(inventory[len(inventory)-1])