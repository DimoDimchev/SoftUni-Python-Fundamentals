import math
from math import ceil

num_students = int(input())
num_lectures = int(input())
bonus_per_lecture = int(input())

# {total bonus}={student attendances}/{course lectures}*(5+{additional bonus})
highest_bonus = 0
best_st_attendance = 0

list_students = [0] * num_students

for student in range(len(list_students)):
    attended = int(input())
    bonus = ceil((attended / num_lectures) * (5 + bonus_per_lecture))
    list_students[student] = bonus
    if bonus == max(list_students):
        highest_bonus = bonus
        best_st_attendance = attended

print(f"Max Bonus: {highest_bonus}.")
print(f"The student has attended {best_st_attendance} lectures.")