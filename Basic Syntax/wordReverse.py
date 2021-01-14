word = input()
reverseWord = ""

for index in range(len(word)-1,-1,-1):
    reverseWord += word[index]

print(reverseWord)