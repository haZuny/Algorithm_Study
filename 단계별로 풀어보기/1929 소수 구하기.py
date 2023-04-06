import sys

m, n = map(int, sys.stdin.readline().split())



for i in range(m, n+1):
    flag = True
    if i == 1:
        flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if(flag):
        print(i)
