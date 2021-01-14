import sys

maxNum = -sys.maxsize

for i in range(1, 4):
    number = int(input())
    if number > maxNum:
        maxNum = number

print(maxNum)
