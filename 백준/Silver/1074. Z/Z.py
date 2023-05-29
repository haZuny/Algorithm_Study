'''
1. 가장 큰 4등분에서 (r,c)가 몇 번째인지 탐색
2. 정답 + 1/4개의 크기 * (순서-1)
3. (r,c)가 포함된 1/4을 기준으로 다시 탐색
'''
n, r, c = map(int, input().split())
ans = 0

while n != 0:
    # 절반 사이즈
    mid = 2**(n-1)
    # (r, c)가 몇번째 인지 탐색
    if r < mid:
        if c <mid:
            idx = 1
        else:
            c -= mid
            idx = 2
    else:
        r -= mid
        if c <mid:
            idx = 3
        else:
            c -= mid
            idx = 4
    # 정답 + 1/4개의 크기 * (순서-1)
    ans += (2**(2*n-2)) * (idx-1)
    
    # (r,c)가 포함된 1/4을 기준으로 다시 탐색
    n -= 1
    
print(ans)