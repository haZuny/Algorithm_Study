import sys

n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))

num = 0
if (1 in ls):
    num = -1



for i in ls:
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break;
    if(flag):
        num += 1
print(num)
