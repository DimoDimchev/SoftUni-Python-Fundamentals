courses = {}

while True:
    command = input()
    if command == "end":
        break
    command_list = command.split(" : ")
    course_name = command_list[0]
    student_name = command_list[1]

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

# courses = dict(sorted(courses, key= lambda x: len(courses[x]), reverse=True))
#
# for (key, value) in courses.items():
#     print(f"{key}: {len(value)}")
#     for index in range(len(value)):
#         print(f"-- {value[index]}")
for course in sorted(courses, key=lambda x: len(courses[x]), reverse=True):
    print(f"{course}: {len(courses[course])}")
    for contestants in sorted(courses[course]):
        print(f"-- {contestants}")