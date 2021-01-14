def action(operator, number1, number2):
    if operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2
    elif operator == "multiply":
        return number1 * number2
    elif operator == "divide":
        return number1 // number2


operator_input = input()

first_number = int(input())
second_number = int(input())

print(action(operator_input, first_number, second_number))
