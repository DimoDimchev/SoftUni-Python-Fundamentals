input_list = input().split()

sorted_list = sorted(input_list, reverse= True)
number = ""

for index in range(len(sorted_list)):
    number += sorted_list[index]

print(int(number))