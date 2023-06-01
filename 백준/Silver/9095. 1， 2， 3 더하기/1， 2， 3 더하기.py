import sys
dp = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n-1])