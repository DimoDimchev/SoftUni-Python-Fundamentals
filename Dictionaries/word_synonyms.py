num_words = int(input())

word_dictionary = {}

for _ in range(num_words):
    word = input()
    synonym = input()
    if word not in word_dictionary:
        word_dictionary[word] = []
    word_dictionary[word].append(synonym)

for word in word_dictionary:
    print(f"{word} - {', '.join(word_dictionary[word])}")