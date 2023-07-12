import sys, math

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

# 절삭평균
# 파이썬 round은 사사오입? 이라 사용하면 에러
try:
    rn = n * 15 / 100
    if rn%1 >= 0.5:
        rn = int(rn//1 + 1)
    else:
        rn = int(rn//1)
    if rn != 0:
        lst = lst[rn:-rn]
    sum = sum(lst)
    aver = sum/(n-(2*rn))
    if aver%1 >= 0.5:
        aver = aver//1 + 1
    else:
        aver = aver//1
    print(int(aver))
except:
    print(0)

