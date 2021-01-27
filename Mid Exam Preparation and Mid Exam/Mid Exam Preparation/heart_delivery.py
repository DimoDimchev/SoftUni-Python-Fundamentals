neighborhood = [int(element) for element in input().split("@")]

command = input()
count_house = 0
successful_houses = 0
unsuccessful_houses = 0

while command != "Love!":
    jump_length = int(command.split()[1])
    count_house += jump_length
    if count_house > len(neighborhood)-1:
        count_house = 0
    if neighborhood[count_house] == 0:
        print(f"Place {count_house} already had Valentine's day.")
    else:
        neighborhood[count_house] -= 2
        if neighborhood[count_house] == 0:
            print(f"Place {count_house} has Valentine's day.")
    command = input()

last_pos = count_house

for house in neighborhood:
    if house == 0:
        successful_houses += 1
    else: unsuccessful_houses += 1

print(f"Cupid's last position was {last_pos}.")
if successful_houses == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {unsuccessful_houses} places.")