char1 = input()
char2 = input()
text = input()

sum = 0

for char in text:
    if ord(char) in range(ord(char1)+1, ord(char2)):
        sum += ord(char)

print(sum)