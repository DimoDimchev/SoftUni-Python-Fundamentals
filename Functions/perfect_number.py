def is_perfect(number):
    number_list = []

    for index in range(1, number):
        if number % index == 0:
            number_list.append(index)

    sum_numbers = sum(number_list)

    if sum_numbers == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number_input = int(input())

is_perfect(number_input)
