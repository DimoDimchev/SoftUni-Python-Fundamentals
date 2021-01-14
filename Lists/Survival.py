import sys

numbers = input()
n = int(input())

list = numbers.split(" ")
list1 = []

for i in range(len(list)):
    list1.append(int(list[i]))

for x in range(1, n + 1):
    smallestNum = min(list1)
    list1.remove(smallestNum)
print(list1)
