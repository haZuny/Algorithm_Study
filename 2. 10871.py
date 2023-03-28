import sys

n, x = map(int, sys.stdin.readline().split())
a = map(int, sys.stdin.readline().split())

for i in a:
    if i < x:
        print("%d "%i, end='')