morse = input().split()
morse_dict = {"..": "I", ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", '.': "E", "..-.": "F", "--.": "G", "....": "H", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..":"Z", "|":" "}

message = ""
for word in morse:
    message += morse_dict[word]

print(message.upper())