combination_list = input().split()
total_sum = 0

for combination in combination_list:
    sum = 0
    number = ""
    for char in combination:
        if char.isdigit():
            number += char
    number = int(number)
    if combination[0].isupper():
        sum += number / (ord(combination[0].lower()) - 96)
    else:
        sum += number * (ord(combination[0].lower()) - 96)

    if combination[len(combination)-1].isupper():
        sum -= (ord(combination[len(combination)-1].lower()) - 96)
    else:
        sum += (ord(combination[len(combination)-1].lower()) - 96)

    total_sum += sum

print(f"{total_sum:.2f}")
