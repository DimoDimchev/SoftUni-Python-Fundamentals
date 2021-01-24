# numbers = [int(element) for element in input().split(", ")]
# indices = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
#
# print(indices)

numbers = list(map(lambda x: int(x), input().split(", ")))
even_indices = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(even_indices)