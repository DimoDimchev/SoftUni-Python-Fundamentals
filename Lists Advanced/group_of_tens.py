input_list = input().split(", ")

boundary = 10

for index in range(len(input_list)):
    while input_list:
        filtered_list = list(filter(lambda x: int(x) <= boundary, input_list))
        filtered_list = [int(element) for element in filtered_list]
        print(f"Group of {boundary}'s: {filtered_list}")
        boundary += 10
        for i in range(len(filtered_list)):
            input_list.remove(str(filtered_list[i]))
        filtered_list = []
