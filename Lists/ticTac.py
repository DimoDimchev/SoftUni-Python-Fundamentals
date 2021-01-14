in1 = input()
in2 = input()
in3 = input()

row1 = [int(num) for num in in1.split(" ")]
row2 = [int(num) for num in in2.split(" ")]
row3 = [int(num) for num in in3.split(" ")]

col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]

diag1 =[row1[0], row2[1], row3[2]]
diag2 =[row1[2], row2[1], row3[0]]

sb_won = 0

if row1.count(1) == 3:
    sb_won = 1
    print("First player won")
elif row1.count(2) == 3:
    sb_won = 1
    print("Second player won")
elif row2.count(1) == 3:
    sb_won = 1
    print("First player won")
elif row2.count(2) == 3:
    sb_won = 1
    print("Second player won")
elif row3.count(1) == 3:
    sb_won = 1
    print("First player won")
elif row3.count(2) == 3:
    sb_won = 1
    print("Second player won")
elif col1.count(1) == 3:
    sb_won = 1
    print("First player won")
elif col1.count(2) == 3:
    sb_won = 1
    print("Second player won")
elif col2.count(1) == 3:
    sb_won = 1
    print("First player won")
elif col2.count(2) == 3:
    sb_won = 1
    print("Second player won")
elif col3.count(1) == 3:
    sb_won = 1
    print("First player won")
elif col3.count(2) == 3:
    sb_won = 1
    print("Second player won")
elif diag1.count(1) == 3:
    sb_won = 1
    print("First player won")
elif diag2.count(2) == 3:
    sb_won = 1
    print("Second player won")

if sb_won == 0:
    print("Draw!")