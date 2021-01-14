quantity = int(input())
days = int(input())

# Ornament Set – 2$ a piece
# Tree Skirt – 5$ a piece
# Tree Garlands – 3$ a piece
# Tree Lights – 15$ a piece

spirit = 0
money = 0

for dayNumber in range(1, days + 1):
    if dayNumber % 11 == 0:
        quantity += 2

    if dayNumber % 2 == 0:
        spirit += 5
        money += (quantity * 2)

    if dayNumber % 3 == 0:
        spirit += 13
        money += (quantity * 5) + (quantity * 3)

    if dayNumber % 5 == 0:
        spirit += 17
        money += (quantity * 15)

        if dayNumber % 3 == 0:
            spirit += 30

    if dayNumber % 10 == 0:
        spirit -= 20
        money += 23

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
