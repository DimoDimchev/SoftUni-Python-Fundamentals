budget = float(input())
priceForKilo = float(input())
priceEggs = 0.75 * priceForKilo
priceMilk = 0.250 * (priceForKilo + ( 0.25 * priceForKilo ))

cozunacs = 0
cozunacPrice = priceEggs + priceMilk + priceForKilo
coloredEggs = 0

while budget > cozunacPrice:
    cozunacs += 1
    budget -= cozunacPrice
    coloredEggs += 3

    if cozunacs % 3 == 0:
        coloredEggs -= (cozunacs - 2)

print(f"You made {cozunacs} cozonacs!", end=" ")
print(f"Now you have {coloredEggs} eggs and "+'{0:.2f}'.format(budget)+"BGN left.")