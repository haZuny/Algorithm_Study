import sys

n, m = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))

answer = -9999

for c1 in range(n-2):
    for c2 in range(c1+1, n-1):
        for c3 in range(c2+1, n):
            three = list[c1] + list[c2] + list[c3]
            if three <= m and answer < three:
                answer = three
print(answer)
