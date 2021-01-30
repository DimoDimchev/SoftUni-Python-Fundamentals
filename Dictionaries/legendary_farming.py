legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
valuable_el = {"shards": 0, "fragments": 0, "motes": 0}

junk = {}

legendary_found = False

while not legendary_found:
    string = input().split(" ")

    for i in range(0, len(string), 2):
        quantity = int(string[i])
        element = string[i + 1].lower()
        if element in valuable_el:
            valuable_el[element] += quantity
        else:
            if element not in junk:
                junk[element] = quantity
            else:
                junk[element] += quantity

        for key, value in valuable_el.items():
            if value >= 250:
                print(f"{legendary[key]} obtained!")
                valuable_el[key] -= 250
                legendary_found = True
                break
        if legendary_found:
            break

sorted_valuable = sorted(valuable_el.items(), key=lambda x: (-x[1], x[0]))
sorted_junk = sorted(junk.items(), key=lambda x: x[0])

for key, value in sorted_valuable:
    print(f"{key}: {value}")
for key, value in sorted_junk:
    print(f"{key}: {value}")
