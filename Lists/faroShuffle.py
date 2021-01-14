elements = input()
n = int(input())

elementList = elements.split(" ")

top = elementList[0]
bottom = elementList[-1]

shuffleCards = []

half = len(elementList) // 2

for i in range(n):
    leftSide = []
    rightSide = []

    for j in range(1, half):
        leftSide.append(elementList[j])

    for z in range(half, len(elementList) - 1):
        rightSide.append(elementList[z])

    for x in range(len(leftSide)):
        shuffleCards.append(rightSide[x])
        shuffleCards.append(leftSide[x])

    elementList = shuffleCards.copy()
    elementList.append(bottom)
    elementList.insert(0, top)
    shuffleCards = []

print(elementList)
