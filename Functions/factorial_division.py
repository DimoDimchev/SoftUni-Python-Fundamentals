def factorial(number1, number2):
    number1_factorial = 1
    number2_factorial = 1
    
    for index in range(number1, 0, -1):
        number1_factorial *= index
    for index in range(number2, 0, -1):
        number2_factorial *= index

    result = number1_factorial / number2_factorial

    print('{0:.2f}'.format(result))


factorial(int(input()), int(input()))

