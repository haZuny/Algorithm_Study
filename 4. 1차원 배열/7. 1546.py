import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
list_new = []

max = max(list)

for i in list:
    list_new.append(i / max * 100)

add = 0
for i in list_new:
    add += i

print(add / n)