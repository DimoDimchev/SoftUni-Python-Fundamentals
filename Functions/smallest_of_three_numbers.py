def find_the_smallest_num(number1, number2, number3):
    min_num = min(number1, number2, number3)
    return min_num


number1_input = int(input())
number2_input = int(input())
number3_input = int(input())

print(find_the_smallest_num(number1_input, number2_input, number3_input))