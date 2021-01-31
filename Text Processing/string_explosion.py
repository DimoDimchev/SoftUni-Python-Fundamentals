word_list = input().split(">")
new_word_list = []
explosion = 0
char = ""

for word in word_list:
    if word[0].isdigit():
        explosion += int(word[0])
        if explosion >= len(word):
            explosion -= len(word)
            char = ">"
        else:
            char = ">" + "".join(word[explosion:])
            explosion = 0
    else:
        char = word
    new_word_list.append(char)

print(''.join(new_word_list))