'''
1*2 0개: 1
1*2 1개: n-2개
1*2 2개: (n-4+2)C2
1*2 x개: (n-2*x+x)Cx

조합: n! / (k! * (n-k)!)

case: 9
0 1
1 8
2 7C2 = 21
3 6C3 = 20
4 5C4 = 5

1 1 3 4 7 11 18 29
'''

fac = [0, 1]

# 팩토리얼 구하기
def getFac(n):    
    if n <= len(fac)-1:
        return fac[n]
    for i in range(len(fac), n+1):
        fac.append(fac[i-1]*i)
    return fac[n]

# 조합 구하기
def getCombi(n, k):
    fac_n = getFac(n)
    fac_k = getFac(k)
    fac_nk = max(1, getFac(n-k))
    return fac_n//(fac_k * fac_nk)

n = int(input())

# 1*2 블럭을 1~최대 선택하는 경우 반영
ans = 0
for i in range(1, n//2+1): # 1*2 0개인 경우는 생략
    ans += getCombi(n - 2*i + i, i)

# 1*2 블럭을 0개 선택하는 경우 추가하여 출
print((ans+1)%10007)