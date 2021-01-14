maxStars= int(input())

star = "*"

for i in range(1, maxStars+1):
    for j in range(0, i):
        print("*", end="")
    print()

for i in range(maxStars-1,0,-1):
    for j in range(0, i):
        print("*", end="")
    print()
