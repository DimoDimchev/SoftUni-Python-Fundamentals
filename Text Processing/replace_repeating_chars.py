word = input()
new_word = ""

for char in word:
    if len(new_word) == 0:
        new_word += char
    else:
        if new_word[len(new_word) - 1] != char:
            new_word += char

print(new_word)