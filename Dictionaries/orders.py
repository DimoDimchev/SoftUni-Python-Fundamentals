product_dict = {}
price_dict = {}

while True:
    command = input()
    if command == "buy":
        break
    command_list = command.split()
    product_name = command_list[0]
    product_price = float(command_list[1])
    product_quantity = int(command_list[2])
    if product_name not in product_dict.keys():
        product_dict[product_name] = product_quantity
    else:
        product_dict[product_name] += product_quantity
    price_dict[product_name] = product_price

for (key, value) in product_dict.items():
    print(f"{key} -> {'{0:.2f}'.format(value * price_dict[key])}")