n = int(input())
word = input()

list1 = []

for i in range(n):
    text = input()
    list1.append(text)
print(list1)

for j in range(len(list1)-1, -1,-1):
    element = list1[j]
    if word not in element:
        list1.remove(element)
print(list1)


