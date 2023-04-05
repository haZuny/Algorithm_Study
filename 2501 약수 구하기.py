import sys

n, k = map(int, sys.stdin.readline().split())

# 약수 체크
m = 0
# 약수 부족한지 체크
flag = True

# k가 0이 될때까지 감
while k != 0:
    m += 1
    # m이 약수이면 k 감수
    if n % m == 0:
        k -= 1
    
    # 약수의 개수가 모자라면 체크
    if n < m:
        flag = False
        break

if flag:
    print(m)
else:
    print(0)
