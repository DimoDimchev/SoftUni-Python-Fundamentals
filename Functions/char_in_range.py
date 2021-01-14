def find_characters(char1, char2):
    for index in range(char1 + 1, char2):
        print(chr(index), end=" ")


char1_input = ord(input())
char2_input = ord(input())

find_characters(char1_input, char2_input)