import sys

n = int(sys.stdin.readline())
list = map(int, sys.stdin.readline().split())
v = int(sys.stdin.readline())

cnt = 0
for i in list:
    if i == v:
        cnt+=1

print(cnt)