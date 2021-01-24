numbers_list = input().split()
middle = int(len(numbers_list) / 2)

left_side = numbers_list[:middle]
right_side = numbers_list[middle + 1:len(numbers_list)]

time_left = 0
time_right = 0

for element in left_side:
    time_left += int(element)
    if element == "0":
        time_left = 0.8 * time_left

for element in right_side:
    time_right += int(element)
    if element == "0":
        time_right = 0.8 * time_right

if time_left < time_right:
    print(f"The winner is left with total time: " + "{:.1f}".format(time_left))
else:
    print(f"The winner is right with total time: " + "{:.1f}".format(time_right))
    