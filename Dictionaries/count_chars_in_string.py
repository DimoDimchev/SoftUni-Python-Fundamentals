word_list = []
word_list[:0] = input()

for letter in word_list:
    if letter == " ":
        word_list.remove(letter)

word_dict = {i: word_list.count(i) for i in word_list}

for (key, value) in word_dict.items():
    print(f"{key} -> {value}")
