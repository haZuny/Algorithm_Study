s = input()
dic = {}
ascA = ord('a')
for i in range(26):
    c = chr(ascA + i)
    dic[c] = [0]
    for j in s:
        dic[c].append(dic[c][-1] + 1 if j == c else dic[c][-1])

q = int(input())

import sys
for _ in range(q):
    a ,l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    print(dic[a][r+1] - dic[a][l])
