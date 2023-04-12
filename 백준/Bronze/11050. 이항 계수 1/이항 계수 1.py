import sys

n, k = map(int, sys.stdin.readline().split())

top = 1
bottom = 1

for i in range(n, n-k, -1):
    top *= i

for i in range(1, k + 1):
    bottom *= i

print(top // bottom)
