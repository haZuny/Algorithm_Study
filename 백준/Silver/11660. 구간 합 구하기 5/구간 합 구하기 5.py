import sys

n, m = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    sumRow = 0
    j = 1
    for num in map(int, sys.stdin.readline().split()):
        dp[i][j] = dp[i-1][j] + sumRow + num
        sumRow += num
        j += 1
        
for _ in range(m):
    i1, j1, i2, j2 = map(int, sys.stdin.readline().split())
    print(dp[i2][j2] - dp[i2][j1-1] - dp[i1-1][j2] + dp[i1-1][j1-1])

        
