resource_dict = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resource_dict:
        resource_dict[resource] = quantity
    else:
        resource_dict[resource] += quantity

for (key, value) in resource_dict.items():
    print(f"{key} -> {value}")