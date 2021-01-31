while True:
    word = input()
    if word == "end":
        break
    else:
        reverse_word = ""
        for char in reversed(word):
            reverse_word += char
        print(f"{word} = {reverse_word}")