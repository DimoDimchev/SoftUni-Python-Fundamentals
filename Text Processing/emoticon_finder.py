text = input()
emoticon = ""
for char in range(len(text)):
    if len(emoticon) > 0:
        emoticon += text[char]
        print(emoticon)
        emoticon = ""
    if text[char] == ":":
        emoticon += ":"