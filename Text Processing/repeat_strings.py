word_list = input().split()
result = ""

for word in word_list:
    result += word * len(word)

print(result)