rows = int(input())

chairs_num = ""

room_number = 0
total_chairs = 0
total_people = 0

more_needed = False

for index in range(rows):
    room_number += 1

    temp_list = input().split()
    number_of_people = sum([int(element) for element in temp_list if "X" not in element])

    chairs = list(filter((lambda x: "X" in x), temp_list))
    for index in range(len(chairs)):
        chairs_num += chairs[index]

    chairs_num = len(list(chairs_num))

    if number_of_people > chairs_num:
        print(f"{number_of_people - chairs_num} more chairs needed in room {room_number}")
        more_needed = True

    total_chairs += chairs_num
    total_people += number_of_people
    chairs_num = ""

if not more_needed:
    print(f"Game On, {total_chairs-total_people} free chairs left")