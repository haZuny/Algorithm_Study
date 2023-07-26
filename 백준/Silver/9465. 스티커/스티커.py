import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    steaker = [[0]+list(map(int, sys.stdin.readline().split()))]
    steaker.append([0]+list(map(int, sys.stdin.readline().split())))

    dp = [[0 for _ in range(n+1)], [0 for _ in range(n+1)]]
    dp[0][1] = steaker[0][1]
    dp[1][1] = steaker[1][1]
    
    for i in range(2, n+1):
        dp[0][i] = max(dp[0][i-2], dp[1][i-1], dp[1][i-2])+steaker[0][i]
        dp[1][i] = max(dp[1][i-2], dp[0][i-1], dp[0][i-2])+steaker[1][i]
    print(max(max(dp[0]), max(dp[1])))
