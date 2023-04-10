import sys

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
dic = {}
for num in list_n:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))
for num in list_m:
    if num in dic:
        print(dic[num], end=' ')
    else:
        print(0, end= ' ')
