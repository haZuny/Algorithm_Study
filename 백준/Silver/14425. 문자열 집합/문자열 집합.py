import sys

n, m = map(int, sys.stdin.readline().split())

set_s = set()
for _ in range(n):
    set_s.add(sys.stdin.readline())

count = 0
for _ in range(m):
    if sys.stdin.readline() in set_s:
        count += 1

print(count)

