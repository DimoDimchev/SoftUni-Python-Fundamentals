food = input().split()
looking_for = input().split()

food_dict = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = food[index + 1]
    food_dict[key] = int(value)

for element in looking_for:
    if element in food_dict.keys():
        print(f"We have {food_dict[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
