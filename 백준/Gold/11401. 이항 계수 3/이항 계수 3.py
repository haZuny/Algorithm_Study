'''
페르마 소정리:
a^p === a
p^(p-1) === 1
p^(p-2) === a^-1

우리 목표:
nCk mod p
= n! / (k! * (n-k)!) mod p

= n! * (k! * (n-k)!)^-1 mod p

= n! mod p * (k! * (n-k)!)^(p-2) mod p ==> 곱하기는 각 과정에서 mod 연산 사용 가능
'''

n, k = map(int, input().split())

# nCk = nCn-k 를 이용하여 범위 축소
if k > n/2:
    k = n-k

# fectorial
nmod = 1
kmod = 1
nkmod = 1
for i  in range(1, n+1):
    nmod *= i
    nmod %= 1000000007

    if i == k:
        kmod = nmod
    if i == (n-k):
        nkmod = nmod

# 거듭제곱 구하기
def multi(num, p):
    if p == 1:
        return num
    
    if p%2 == 0:
        return (multi(num, p//2) ** 2) % 1000000007
    return (num * multi(num, p//2) ** 2) % 1000000007

bottom = multi(kmod * nkmod, 1000000005)

print((nmod * bottom)%1000000007)
