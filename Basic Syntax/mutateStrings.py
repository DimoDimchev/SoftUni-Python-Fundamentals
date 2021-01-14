word1 = input()
word2 = input()

result = ""
prev = word1

for i in range(len(word1)):
    for j in range(0, i+1):
        result += word2[j]
    for z in range(i+1, len(word1)):
        result += word1[z]
    if prev != result:
        print(result)
    prev = result
    result = ""