import sys

n = int(sys.stdin.readline())
dic = {}
for _ in range(n):
    y, x = map(int, sys.stdin.readline().split())
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]
for x in sorted(dic):
    ys = dic[x]
    ys.sort()
    for y in ys:
        print(y, x)
