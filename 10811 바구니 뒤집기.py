import sys

n, m = map(int, sys.stdin.readline().split())
list = [i+1 for i in range(n)]
for repeat in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    while(i < j):
        list[i], list[j] = list[j], list[i]
        i += 1
        j -= 1
print(*list)
