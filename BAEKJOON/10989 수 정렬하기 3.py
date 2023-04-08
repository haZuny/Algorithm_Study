import sys

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    num = int(sys.stdin.readline())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
for i in sorted(dic):
    for _ in range(dic[i]):
        print(i)
