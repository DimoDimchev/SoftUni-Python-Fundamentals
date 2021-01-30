products = {}
sum_quantities = 0
command = input()

while command != "statistics":
    command_list = command.split(":")
    product = command_list[0]
    quantity = int(command_list[1])
    sum_quantities += quantity
    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    command = input()

total_products = len(products)
print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {sum_quantities}")