input_list1 = input().split(", ")
input_list2 = input().split(", ")

#result_list = [input_list1[index] for index in range(len(input_list1)) if input_list1[index] in input_list2[]]

result_list = []

for index in range(len(input_list1)):
    current_element = input_list1[index]
    for index in range(len(input_list2)):
        if current_element in input_list2[index]:
            if current_element not in result_list:
                result_list.append(current_element)

print(result_list)