n, m = map(int, input().split())
sumLst = [0]
for i in map(int, input().split()):
    sumLst.append(sumLst[-1]+i)

import sys
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sumLst[j] - sumLst[i-1])
