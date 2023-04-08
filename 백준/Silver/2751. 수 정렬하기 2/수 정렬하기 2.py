import sys

n = int(sys.stdin.readline())

ls = []

for _ in range(n):
    ls.append(int(sys.stdin.readline()))

ls.sort()

for k in ls:
    print(k)
