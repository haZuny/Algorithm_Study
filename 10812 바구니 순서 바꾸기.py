import sys


n, m = map(int, sys.stdin.readline().split())
list = [i for i in range(1, n+1)]
print(list)

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    k -= 1
    temp = list[i:k]
    list[i:i+j+1-k] = list[k:j+1]
    list[i+j+1-k:j+1] = temp

for i in list:
    print(i, end=' ')
