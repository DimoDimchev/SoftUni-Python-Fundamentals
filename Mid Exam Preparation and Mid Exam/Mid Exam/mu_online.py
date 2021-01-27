health = 100
bitcoins = 0

dungeon = input().split("|")
died = False

for room in dungeon:
    command_list = room.split()
    command = command_list[0]
    points = int(command_list[1])

    if command == "potion":
        if (health + points) <= 100:
            health += points
        elif health + points > 100:
            points = 100 - health
            health += points
        print(f"You healed for {points} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")
    else:
        health -= points
        if health > 0:
            print(f"You slayed {command}.")
        else:
            died = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {dungeon.index(room)+1}")
            break

if not died:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")