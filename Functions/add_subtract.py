def add_and_subtract():
    def sum_numbers(number1, number2):
        result_addition = number1 + number2
        return result_addition

    def subtract(number3):
        result = sum_numbers(number1_input, number2_input) - number3
        return result

    number1_input = int(input())
    number2_input = int(input())
    number3_input = int(input())

    print(subtract(number3_input))


add_and_subtract()
