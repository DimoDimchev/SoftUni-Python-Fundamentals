tabs = int(input())
salary = int(input())

for i in range(1, tabs + 1):
    page = input()
    if page == "Facebook":
        salary = salary - 150
    if page == "Instagram":
        salary = salary - 100
    if page == "Reddit":
        salary = salary - 50
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
