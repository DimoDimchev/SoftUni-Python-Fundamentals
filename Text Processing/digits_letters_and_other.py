word_to_filter = input()

digits = ""
letters = ""
other = ""

for char in word_to_filter:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(digits)
print(letters)
print(other)