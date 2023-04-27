n = int(input())
lst = list(map(int, input().split()))
dp_big = [1] * n
dp = [1] * n

for i in range(n):
    num = lst[i]
    
    for j in range(i):
        if num > lst[j]:
            dp_big[i]  = max(dp_big[i], dp_big[j]+1)

    dp[i] = max(dp[i], dp_big[i])
    
    for j in range(i, n):
        num = lst[j]
        for k in range(i, j):
            if lst[k] > num:
                dp[j] = max(dp[j], dp[k]+1)

print(max(dp))
