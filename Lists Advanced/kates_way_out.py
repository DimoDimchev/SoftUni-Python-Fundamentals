levels = int(input())

maze = [list(input()) for _ in range(levels)]

count_moves = 0
empty = " "

exited = False

for row in maze:
    if "k" in row:
        location = row.index("k")
        level = maze.index(row)
        break
for row in maze:
    for el in row:
        if el == empty:
            count_moves += 1
while True:

    if location == 0 or location == len(maze[0]) - 1 or level == 0 or level == levels - 1:
        count_moves += 1
        exited = True
        break

    left_element = maze[level][location-1]
    right_element = maze[level][location+1]
    above_element = maze[level - 1][location]
    below_element = maze[level + 1][location]

    if left_element == "#" and right_element == "#" and above_element == "#" and below_element == "#":
        break
    else:
        if left_element == " ":
            maze[level][location] = "#"
            location = location - 1
        elif right_element == " ":
            maze[level][location] = "#"
            location = location + 1
        elif above_element == " ":
            maze[level][location] = "#"
            level = level - 1
        elif below_element == " ":
            maze[level][location] = "#"
            level = level + 1
if exited:
    print(f"Kate got out in {count_moves} moves")
else:
    print("Kate cannot get out")

