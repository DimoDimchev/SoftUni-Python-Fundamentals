word_to_remove = input()
word_to_remove_from = input()

while word_to_remove in word_to_remove_from:
    word_to_remove_from = word_to_remove_from.replace(word_to_remove, "")

print(word_to_remove_from)