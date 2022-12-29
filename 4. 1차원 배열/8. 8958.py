import sys

n = int(sys.stdin.readline())

list = []

for i in range(n):
    list.append(sys.stdin.readline())

for i in list:
    point = 0
    bonus = 0
    for j in i:
        if j == 'O':
            bonus += 1
            point += bonus
        else:
            bonus = 0
    print(point)