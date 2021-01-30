words = input().lower().split()

word_dictionary = {}

for word in words:
    if word not in word_dictionary:
        word_dictionary[word] = 0
    word_dictionary[word] += 1

for (key, value) in word_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")