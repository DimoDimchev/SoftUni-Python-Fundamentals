sequence = input().split()

command = input()
moves = 0
won = False

while command != "end":
    moves += 1
    command_list = [int(el) for el in command.split()]
    element1 = command_list[0]
    element2 = command_list[1]
    if element1 == element2 or element1 > len(sequence) - 1 or element2 > len(sequence) - 1 or element1 < 0 or element2 < 0:
        print("Invalid input! Adding additional elements to the board")
        middle = len(sequence) // 2
        sequence.insert(middle, f"-{moves}a")
        sequence.insert(middle, f"-{moves}a")
    elif sequence[element1] == sequence[element2]:
        print(f"Congrats! You have found matching elements - {sequence[element1]}!")
        sequence = list(filter(lambda x: x != sequence[element1], sequence))
    else:
        print("Try again!")
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        won = True
        break
    command = input()

if not won:
    print(f"Sorry you lose :(")
    print(' '.join(sequence))
