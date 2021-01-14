numbers = input()

list1 = numbers.split(" ")
list2 = []

for i in range(len(list1)):

    currentNum = int(list1[i])

    if currentNum < 0:
        list2.append(abs(currentNum))
    elif currentNum > 0:
        list2.append(-currentNum)
    else:
        list2.append(0)

print(list2)
