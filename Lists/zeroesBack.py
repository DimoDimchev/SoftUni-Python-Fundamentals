numbers = input()

numbersList = [int(num) for num in numbers.split(", ")]

zeros = 0

while 0 in numbersList:
    zeros += 1
    numbersList.remove(0)

for i in range(zeros):
    numbersList.append(0)

print(numbersList)
