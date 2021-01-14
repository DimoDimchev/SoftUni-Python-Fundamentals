n = int(input())

positive = []
negative = []

positiveCount= 0
negativeSum = 0

for i in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
        positiveCount += 1
    else:
        negative.append(number)
        negativeSum += number

print(positive)
print(negative)
print(f"Count of positives: {positiveCount}. Sum of negatives: {negativeSum}")

