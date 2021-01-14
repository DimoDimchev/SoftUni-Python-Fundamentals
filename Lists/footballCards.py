cards = input()

list1 = cards.split(" ")
list2 = []

team1 = 11
team2 = 11

for i in range(len(list1)):
    if team1 < 7 or team2 < 7:
        print("Game was terminated")
    if "A" in list1[i] and list1[i] not in list2:
        team1 -= 1
        list2.append(list1[i])
    elif "B" in list1[i] and list1[i] not in list2:
        team2 -= 1
        list2.append(list1[i])

print(f"Team A - {team1}; Team B - {team2}")

if team1 < 7 or team2 < 7:
    print("Game was terminated")