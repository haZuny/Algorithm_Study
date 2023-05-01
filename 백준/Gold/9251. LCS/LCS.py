'''
ACAYKPADF
FGCAPCAK

ACAYKP
CAPCAK
부분수열: 알파벳 순서가 일치

  0 A C A Y K P 
0 0 0 0 0 0 0 0
C 0 0 1 1 1 1 1
A 0 1 1 2 1 1 1
P 0 0 1 1 2 1 2
C 0 0 2 2 2 2 2
A 0 1 1 3 
K 0

  0 A A A B B C
0 0 0 0 0 0 0 0
A 0 1 1 1 1 1 1
A 0 1 2 2 2 2 2
B 0 1 2 2 3 3 3
C 0 1 2 2 3 3 4

[i][j] = max(자신 이전까지 세로 중 최대, 마지막에 더한 값), 같은 문자 나오면 +1

ACAA
AAACBA

AAABBC
AABC

ABCBD
ACBD

'''

def printDP():
    print('  0 '+ ' '.join(map(str, s2)))
    idx = 0
    for l1 in dp:
        if idx == 0:
            print('0 ', end='')
        else:
            print(s1[idx-1], end=' ')
        print(' '.join(map(str, l1)))
        idx += 1


s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
maxRow = [0 for _ in range(len(s2)+1)]

for i in range(1, len(dp)): # i: s1 idx
    lastAdd = 0
    for j in range(1, len(dp[0])):  # j: s2 idx
        if s1[i-1] == s2[j-1]:
            lastAdd = max(maxRow[j-1]+ 1, lastAdd) 
            dp[i][j] = lastAdd
        else:
            lastAdd = max(maxRow[j-1], lastAdd)
            dp[i][j] = lastAdd
            
    # maxRow 업데이트
    for j in range(1, len(dp[0])):
        if maxRow[j] < dp[i][j]:
            maxRow[j] = dp[i][j]
        
#printDP()
#print(maxRow)
print(max(maxRow))
