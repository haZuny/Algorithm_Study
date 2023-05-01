s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
maxRow = [0 for _ in range(len(s2)+1)]

for i in range(1, len(dp)): # i: s1 idx
    lastAdd = 0
    for j in range(1, len(dp[0])):  # j: s2 idx
        if s1[i-1] == s2[j-1]:
            lastAdd = max(maxRow[j-1] + 1, lastAdd) 
            dp[i][j] = lastAdd
        else:
            lastAdd = max(maxRow[j-1], lastAdd)
            dp[i][j] = lastAdd
            
    # maxRow 업데이트
    for j in range(1, len(dp[0])):
        if maxRow[j] < dp[i][j]:
            maxRow[j] = dp[i][j]
        
print(max(maxRow))
