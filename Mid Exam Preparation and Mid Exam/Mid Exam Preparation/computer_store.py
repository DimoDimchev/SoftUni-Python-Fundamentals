command = input()

total_price = 0
taxes_price = 0
final_price = 0

while command not in ["special", "regular"]:
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price
        taxes_price += price * 0.2
    command = input()

if total_price > 0:
    if command == "special":
        final_price = (total_price + taxes_price) * 0.9
    else:
        final_price = total_price + taxes_price
    print("Congratulations you've just bought a new computer!")
    print("Price without taxes: " + '{0:.2f}'.format(total_price) + "$")
    print(f"Taxes: " + '{0:.2f}'.format(taxes_price) + "$")
    print("-----------")
    print(f"Total price: " + '{0:.2f}'.format(final_price) + "$")
else:
    print("Invalid order!")
