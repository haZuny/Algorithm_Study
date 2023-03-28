import sys

list = []
for i in range(9):
    list.append(int(sys.stdin.readline()))
maxNum = max(list)
print(maxNum)
print(list.index(maxNum)+1)