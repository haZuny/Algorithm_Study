import sys

n = int(sys.stdin.readline())
arr = [[False for j in range(100)] for i in range(100)]

cnt = 0

for _ in range(n):
    left, bottom = map(int, sys.stdin.readline().split())
    for i in range(left, 10 + left):
        for j in range(bottom, 10 + bottom):
            if not arr[i][j]:
                cnt += 1
                arr[i][j] = True
print(cnt)
