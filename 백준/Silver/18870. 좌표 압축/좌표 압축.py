import sys

n = int(sys.stdin.readline())
dic = {}
list = list(map(int, sys.stdin.readline().split()))

for num in list:
    if not num in dic:
        dic[num] = 0

sortDic = sorted(dic)

for i in range(len(sortDic)):
    dic[sortDic[i]] = i

for num in list:
    print(dic[num], end=' ')
