'''
      0  1  2  3  4  5  6  7
      
0     0  0  0  0  0  0  0  0
6,13  0  0  0  0  0  0  13 13
4,8   0  0  0  0  8  8  13 13
3,6   0  0  0  6  8  8  13 14
5,12  0  0  0  6  8  12 13 14

'''

n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]  # 가로: 무게, 세로: 물건들

for i in range(1,n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
#print(dp)
print(dp[-1][-1])
