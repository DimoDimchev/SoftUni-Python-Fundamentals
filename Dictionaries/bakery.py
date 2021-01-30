food = input().split()
food_dict = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = food[index + 1]
    food_dict[key] = int(value)

print(food_dict)