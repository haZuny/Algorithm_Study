# 최소 개수: dp[n-임의의 제곱수]+1
# 가장큰 제곱수부터 최소값 탐색
import math
n = int(input())
dp = [float('inf') for _ in range(n+1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    biggest = int(math.sqrt(i))
    minRest = dp[i-biggest**2]
    for j in range(1, biggest):
        temp = dp[i-j**2]
        minRest = min(minRest, temp)
    dp[i] = minRest+1

print(dp[n])
