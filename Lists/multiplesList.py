factor = int(input())
count = int(input())

list1 = []

for i in range(1, count+1):
    number = i * factor
    list1.append(number)

print(list1)
