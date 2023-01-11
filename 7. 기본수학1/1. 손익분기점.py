import sys

a, b, c = map(int, sys.stdin.readline().split())

purePrice = c - b
if purePrice > 0:
    print(a // purePrice + 1)
else:
    print(-1)
