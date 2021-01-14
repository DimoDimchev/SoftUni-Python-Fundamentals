def repeat(word, times_repeated):
    for i in range(times_repeated):
        print(word, end="")


word_input = input()
number = int(input())

repeat(word_input, number)