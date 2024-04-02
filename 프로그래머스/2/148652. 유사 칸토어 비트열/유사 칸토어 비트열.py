'''
              1                     0
            11011                   1
11011 11011 00000 11011 11011       2
11011 11011 00000 11011 11011     11011 11011 00000 11011 11011     11011 11011 00000 11011 11011     11011 11011 00000 11011 11011     11011 11011 00000 11011 11011
'''
# 주어진 인덱스 까지의 1의 개수 탐색, idx: 리스트의 인덱스 기준
def getCntUntilIdx(idx, n, dp):
        if n < 0: return 0;
        if n == 0: return 1;
        if n == 1:
            if idx == 0: return 1;
            if idx == 1: return 2;
            if idx == 2: return 2;
            if idx == 3: return 3;
            if idx == 4: return 4;
        
        # 몫과 나머지 계산
        div = idx//(5**(n-1))
        remain = idx%(5**(n-1))
        # 00000 기준으로 케이스를 나눠서, 재귀적으로 개수를 구함
        if div < 2:
            return dp[n-1]*div + getCntUntilIdx(remain, n-1, dp)
        elif div == 2:
            return dp[n-1]*div
        else:
            return dp[n-1]*(div-1) + getCntUntilIdx(remain, n-1, dp)
            
def solution(n, l, r):
    # 각 단계별로 1이 몇개 있는지 기록
    dp = [1 for i in range(n+1)]
    for i in range(1, n+1):
        dp[i] = dp[i-1]*4
    
    answer = getCntUntilIdx(r-1, n, dp) - getCntUntilIdx(l-2, n, dp)
    
    return answer