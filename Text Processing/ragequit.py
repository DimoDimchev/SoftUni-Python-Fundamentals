text = input()

string_to_print = ""
total_print = ""
char = 0

while char < len(text):
    if not text[char].isdigit():
        string_to_print += text[char]
        char += 1
    else:
        number = ""
        while char < len(text) and text[char].isdigit():
            number += text[char]
            char += 1
        total_print += string_to_print.upper() * int(number)
        string_to_print = ""

unique_symbols = len(list(filter(lambda x: not x.isdigit(), set(total_print.lower()))))

print(f"Unique symbols used: {unique_symbols}")
print(total_print)
