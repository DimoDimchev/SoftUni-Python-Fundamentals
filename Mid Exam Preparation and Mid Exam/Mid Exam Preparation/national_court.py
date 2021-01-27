efficiency = 0
total_time = 0
take_break = 1

for _ in range(3):
    efficiency += int(input())

people = int(input())

while people > 0:
    if (total_time + 1) % 4 == 0:
        total_time += 1
    else:
        total_time += 1
        people -= efficiency

print(f"Time needed: {total_time}h.")