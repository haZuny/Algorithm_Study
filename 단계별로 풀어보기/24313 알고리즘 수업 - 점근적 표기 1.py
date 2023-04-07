import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

flag = 1
# 직선 기울기 체크
if n0 * c< a1:
    flag = 0
# x=n0에서의 위치 체크
if a1 * n0 + a0 > c * n0:
    flag = 0

print(flag)
