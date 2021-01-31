words_list = input().split()
word1 = words_list[0]
word2 = words_list[1]
sum = 0

while len(word1) != 0 and len(word2) != 0:
    sum += ord(word1[0]) * ord(word2[0])
    word1 = word1[1:]
    word2 = word2[1:]
if len(word1) > len(word2):
    for char in word1:
        sum += ord(char)
elif len(word2) > len(word1):
    for char in word2:
        sum += ord(char)
print(sum)