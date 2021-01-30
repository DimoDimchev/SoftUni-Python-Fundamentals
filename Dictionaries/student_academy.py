number = int(input())
student_dict = {}
filtered_students = {}

for _ in range(number):
    student_name = input()
    student_grade = float(input())
    if student_name not in student_dict:
        student_dict[student_name] = []
    student_dict[student_name].append(student_grade)

for (key, value) in student_dict.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        filtered_students[key] = average_grade
        # print(f"{key} -> {average_grade:.2f}")

for student, grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {grade:.2f}")
