n = int(input())

lst = []
cnts = []

for _ in range(n):
    x, y = map(int, input().split())
    lst.append([x, y, 0])

for i in range(n):
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            lst[i][2] += 1

for i in lst:
    print(i[2]+1, end=' ')
