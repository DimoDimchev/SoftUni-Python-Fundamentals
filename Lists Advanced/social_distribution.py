# population = [int(element) for element in input().split(", ")]
# min_wealth = int(input())

# all_money = sum(population)
#
# # finds the people with less than the minimum wealth and the ones with more
# poor = list(filter(lambda x: x < min_wealth, population))
# rich = sorted(list(filter(lambda x: x > min_wealth, population)), reverse=True)
#
# count = 0
#
# if all_money // min_wealth < len(population):
#     print("No equal distribution possible")
# else:
#     # removes the poor and the rich from the list
#     for index in range(len(poor)):
#         population.remove(poor[index])
#     for index in range(len(rich)):
#         population.remove(rich[index])
#
#     # distributes the money evenly
#     while sum(poor) != len(poor) * min_wealth:
#         if count > len(poor) - 1:
#             count = 0
#         if poor[count] == min_wealth:
#             population.append(poor[count])
#             poor.pop(count)
#             count = 0
#         if rich[0] > min_wealth:
#             poor[count] += 1
#             rich[0] -= 1
#         else:
#             population.append(rich[0])
#             rich.pop(0)
#         count += 1
#
#     rich = sorted(rich)
#
#     # inserts the poor and the rich back in the list
#     for index in range(len(poor)):
#         population.insert(0, poor[index])
#     for index in range(len(rich)):
#         population.append(rich[index])
#
#     print(population)

population = [int(element) for element in input().split(", ")]
min_wealth = int(input())

possible = True

for i in range(len(population)):
    biggest_num = max(population)
    if population[i] < min_wealth:
        difference = min_wealth - population[i]
        population[i] += difference
        if population[population.index(biggest_num)] - difference < min_wealth:
            possible = False
            break
        else:
            population[population.index(biggest_num)] -= difference
            biggest_num = max(population)
        if population[population.index(biggest_num)] < min_wealth:
            is_Possible = False
            break
if possible:
    print(population)
else:
    print("No equal distribution possible")