import sys

# N: 바구니 개수
# M: 공을 넣은 횟수
n, m = map(int, sys.stdin.readline().split())

list = [0] * n
for repeat in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    while(i <= j):
        list[i-1] = k
        i += 1

for i in list:
    print(i, end=' ')
