def order(product, times_ordered):
    final_price = 0

    for i in range (times_ordered):
        if product == "coffee":
            final_price += 1.50
        elif product == "water":
            final_price += 1.00
        elif product == "coke":
            final_price += 1.40
        elif product == "snacks":
            final_price += 2.00

    return final_price


product_input = input()
number = int(input())

print('{0:.2f}'.format(order(product_input, number)))
