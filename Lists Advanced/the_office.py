employees_list = [int(x) for x in (input().split(" "))]
HIF = int(input()) # happiness improvement factor

happy_count = 0

increased_happiness_list = list(map(lambda employee: employee * HIF, employees_list))
average_happiness = sum(increased_happiness_list) / len(increased_happiness_list)
happy_list = list(filter(lambda employee: employee >= average_happiness, increased_happiness_list))

for i in range(len(happy_list)):
    happy_count += 1

if happy_count >= len(employees_list)/2:
    print(f"Score: {happy_count}/{len(employees_list)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(employees_list)}. Employees are not happy!")