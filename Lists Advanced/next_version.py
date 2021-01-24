input_list = input().split(".")
number = ""

for index in range(len(input_list)):
    number += input_list[index]

result = int(number) + 1
result_list = list(str(result))

print(f"{result_list[0]}.{result_list[1]}.{result_list[2]}")