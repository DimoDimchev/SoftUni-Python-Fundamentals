def odd_even_sum(number):
    digits = [int(x) for x in str(number)]
    even_sum = 0
    odd_sum = 0
    for index in range(len(digits)):
        if digits[index] % 2 == 0:
            even_sum += digits[index]
        else:
            odd_sum += digits[index]

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number_input = int(input())

odd_even_sum(number_input)