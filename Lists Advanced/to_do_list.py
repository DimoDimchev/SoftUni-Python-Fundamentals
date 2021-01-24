command = input()

notes = [0 for _ in range(10)]

while command != "End":
    element = command.split("-")
    importance = int(element[0])
    note = element[1]
    notes.insert(importance, note)
    command = input()

result = [task for task in notes if task != 0 ]

print(result)