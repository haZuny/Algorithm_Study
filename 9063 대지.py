# 땅의 넓이: (가장 오른쪽 - 가장 왼쪽) * (가장 위쪽 - 가장 아랬쪽)
import sys

n = int(sys.stdin.readline())
x_min = 99999999
x_max = -99999999
y_min = 99999999
y_max = -99999999

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x < x_min:
        x_min = x
    if x > x_max:
        x_max = x
    if y_min > y:
        y_min = y
    if y_max < y:
        y_max = y

print((x_max - x_min) * (y_max-y_min))
