unwanted_words = input().split(", ")
text_to_filter = input()

for word in unwanted_words:
    while word in text_to_filter:
        text_to_filter = text_to_filter.replace(word, len(word) * "*")

print(text_to_filter)