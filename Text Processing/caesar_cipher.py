word = input()

new_word = ""
for char in word:
    char = chr(ord(char)+3)
    new_word += char
print(new_word)
