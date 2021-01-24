numbers_list = input().split(" ")
word_list = list(input())

result = ""

# finds the sum of all digits
for element in numbers_list:
    numbers_sum = 0
    for number in element:
        numbers_sum += int(number)
    # prints the letter, corresponding to the index
    if numbers_sum >= len(word_list):
        while True:
            numbers_sum -= len(word_list)
            if numbers_sum < len(word_list):
                break
    result += word_list[numbers_sum]
    word_list.pop(numbers_sum)
print(result)
