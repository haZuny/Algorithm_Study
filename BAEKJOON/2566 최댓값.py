import sys

maxNum = 0
maxRow = 0
maxColumn = 0

for i in range(9):
    ls = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if maxNum < ls[j]:
            maxNum = ls[j]
            maxRow = i
            maxColumn = j

print(maxNum)
print(maxRow+1, maxColumn+1)
