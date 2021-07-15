import re
n = list(input())
for k in n:
    if (len(n[k]) == 16 or (len(n[k]) == 19 and n[k].count("-") == 3)) and (n[k][0] == 4 or n[k][0] == 5 or n[k][0] == 6):
        for x in n[k]:
            if (n[k][x] >= 0 and n[k][x] <= 9) or n[k][x] == "-":
                continue
            else:
                print("False")
print("True")
