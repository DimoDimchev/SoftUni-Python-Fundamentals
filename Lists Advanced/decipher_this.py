given_word = input().split()

for element in given_word:
    # divides the word into letters only
    list_of_letters = []
    list_of_letters[:0] = element
    list_of_letters = list(filter(lambda x: x.isalpha(), list_of_letters))

    # finds the character code
    list_of_characters = list(filter(lambda x: x.isdigit(), element))
    list_of_characters = int(''.join(list_of_characters))
    encoded_letter = chr(list_of_characters)

    # swaps the second element with the last one
    list_of_letters[0], list_of_letters[len(list_of_letters)-1] = list_of_letters[len(list_of_letters)-1], list_of_letters[0]

    # adds encoded letter back into list
    list_of_letters.insert(0, encoded_letter)

    # prints each word
    print(''.join(list_of_letters), end=" ")